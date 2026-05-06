from __future__ import annotations

import streamlit as st

from database import (
    add_item,
    authenticate_user,
    create_shopping_list,
    create_user,
    get_items,
    get_list_for_user,
    get_shopping_lists,
    init_db,
    set_item_done,
)


st.set_page_config(page_title="GroupQuest Einkaufsapp", page_icon="GQ", layout="centered")
init_db()


def get_current_user() -> dict | None:
    return st.session_state.get("user")


def login_user(user_id: int, username: str) -> None:
    st.session_state.user = {"id": user_id, "username": username}
    st.session_state.active_list_id = None


def logout_user() -> None:
    st.session_state.pop("user", None)
    st.session_state.pop("active_list_id", None)


def render_auth() -> None:
    st.title("GroupQuest Einkaufsapp")
    st.caption("Sprint-1-Prototyp mit Streamlit und SQLite")

    login_tab, register_tab = st.tabs(["Login", "Registrieren"])

    with login_tab:
        with st.form("login-form"):
            username = st.text_input("Benutzername", key="login-username")
            password = st.text_input("Passwort", type="password", key="login-password")
            submitted = st.form_submit_button("Einloggen")

        if submitted:
            user = authenticate_user(username, password)
            if user:
                login_user(user["id"], user["username"])
                st.rerun()
            else:
                st.error("Login fehlgeschlagen. Pruefe Benutzername und Passwort.")

    with register_tab:
        with st.form("register-form"):
            username = st.text_input("Benutzername", key="register-username")
            password = st.text_input("Passwort", type="password", key="register-password")
            submitted = st.form_submit_button("Account erstellen")

        if submitted:
            ok, message = create_user(username, password)
            if ok:
                st.success(message)
            else:
                st.error(message)


def render_sidebar(user: dict) -> None:
    with st.sidebar:
        st.subheader(f"Angemeldet als {user['username']}")
        if st.button("Logout"):
            logout_user()
            st.rerun()

        st.divider()
        st.subheader("Neue Einkaufsliste")
        with st.form("new-list-form", clear_on_submit=True):
            list_name = st.text_input("Listenname", placeholder="z. B. Wochenendeinkauf")
            submitted = st.form_submit_button("Liste erstellen")

        if submitted:
            if list_name.strip():
                create_shopping_list(user["id"], list_name)
                st.success("Einkaufsliste erstellt.")
                st.rerun()
            else:
                st.warning("Bitte gib einen Namen ein.")


def render_list_selector(user: dict) -> list:
    lists = get_shopping_lists(user["id"])
    st.subheader("Meine Einkaufslisten")

    if not lists:
        st.info("Noch keine Einkaufsliste vorhanden. Erstelle links deine erste Liste.")
        return lists

    options = {entry["id"]: entry for entry in lists}
    current_id = st.session_state.get("active_list_id")
    if current_id not in options:
        current_id = lists[0]["id"]
        st.session_state.active_list_id = current_id

    selected_id = st.selectbox(
        "Liste auswaehlen",
        options=list(options.keys()),
        index=list(options.keys()).index(current_id),
        format_func=lambda list_id: options[list_id]["name"],
    )
    st.session_state.active_list_id = selected_id

    cols = st.columns(3)
    cols[0].metric("Listen", len(lists))
    cols[1].metric("Artikel gesamt", sum(row["item_count"] or 0 for row in lists))
    cols[2].metric("Offen", sum(row["open_count"] or 0 for row in lists))

    return lists


def render_items(user: dict, list_id: int) -> None:
    shopping_list = get_list_for_user(user["id"], list_id)
    if not shopping_list:
        st.warning("Diese Liste gehoert nicht zu deinem Account.")
        return

    st.divider()
    st.header(shopping_list["name"])

    with st.form("new-item-form", clear_on_submit=True):
        col_name, col_quantity = st.columns([2, 1])
        item_name = col_name.text_input("Artikel", placeholder="z. B. Milch")
        quantity = col_quantity.text_input("Menge", placeholder="z. B. 2 l")
        submitted = st.form_submit_button("Artikel hinzufuegen")

    if submitted:
        if item_name.strip():
            add_item(list_id, item_name, quantity)
            st.success("Artikel hinzugefuegt.")
            st.rerun()
        else:
            st.warning("Bitte gib einen Artikelnamen ein.")

    items = get_items(list_id)
    open_items = [item for item in items if not item["is_done"]]
    done_items = [item for item in items if item["is_done"]]

    stat_cols = st.columns(3)
    stat_cols[0].metric("Offen", len(open_items))
    stat_cols[1].metric("Erledigt", len(done_items))
    stat_cols[2].metric("Gesamt", len(items))

    st.subheader("Offene Artikel")
    if not open_items:
        st.info("Keine offenen Artikel.")
    for item in open_items:
        label = item["name"] if not item["quantity"] else f"{item['name']} ({item['quantity']})"
        if st.checkbox(label, value=False, key=f"open-{item['id']}"):
            set_item_done(item["id"], True)
            st.rerun()

    with st.expander("Erledigte Artikel", expanded=bool(done_items)):
        if not done_items:
            st.caption("Noch nichts abgehakt.")
        for item in done_items:
            label = item["name"] if not item["quantity"] else f"{item['name']} ({item['quantity']})"
            checked = st.checkbox(label, value=True, key=f"done-{item['id']}")
            if not checked:
                set_item_done(item["id"], False)
                st.rerun()


def main() -> None:
    user = get_current_user()
    if not user:
        render_auth()
        return

    render_sidebar(user)
    st.title("Einkauf planen")
    st.caption("Sprint 1: Registrierung, Login, Listen, Artikel und Fortschritt.")
    lists = render_list_selector(user)
    active_list_id = st.session_state.get("active_list_id")
    if lists and active_list_id:
        render_items(user, active_list_id)


if __name__ == "__main__":
    main()
