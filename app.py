from __future__ import annotations

import streamlit as st

from database import (
    add_item,
    authenticate_user,
    create_shopping_list,
    create_user,
    delete_item,
    delete_shopping_list,
    get_items,
    get_list_for_user,
    get_shopping_lists,
    init_db,
    set_item_done,
    update_item,
    update_shopping_list,
)


st.set_page_config(page_title="GroupQuest Einkaufsapp", page_icon="GQ", layout="centered")
init_db()

CATEGORIES = ["Obst & Gemuese", "Kuehlregal", "Backwaren", "Getraenke", "Drogerie", "Sonstiges"]


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
    st.caption("Sprint-2-Prototyp mit Streamlit und SQLite")

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


def render_list_actions(user: dict, list_id: int, current_name: str) -> None:
    st.subheader("Einkaufsliste verwalten")
    next_name = st.text_input("Neuer Listenname", value=current_name, key=f"rename-list-{list_id}")
    if st.button("Liste umbenennen", key=f"rename-list-button-{list_id}"):
        if next_name.strip():
            update_shopping_list(user["id"], list_id, next_name)
            st.success("Einkaufsliste wurde umbenannt.")
            st.rerun()
        else:
            st.warning("Der Listenname darf nicht leer sein.")

    confirm_delete = st.checkbox(
        "Ich moechte diese Einkaufsliste wirklich loeschen.",
        key=f"confirm-delete-list-{list_id}",
    )
    if st.button("Liste loeschen", disabled=not confirm_delete):
        delete_shopping_list(user["id"], list_id)
        st.session_state.active_list_id = None
        st.success("Einkaufsliste wurde geloescht.")
        st.rerun()


def item_label(item) -> str:
    label = item["name"]
    if item["quantity"]:
        label = f"{label} ({item['quantity']})"
    if item["category"]:
        label = f"{label} - {item['category']}"
    return label


def render_item_editor(item) -> None:
    with st.expander(f"Bearbeiten: {item['name']}"):
        with st.form(f"edit-item-{item['id']}"):
            item_name = st.text_input("Artikelname", value=item["name"])
            quantity = st.text_input("Menge", value=item["quantity"] or "")
            category_options = [""] + CATEGORIES
            current_category = item["category"] or ""
            category = st.selectbox(
                "Kategorie",
                options=category_options,
                index=category_options.index(current_category)
                if current_category in category_options
                else 0,
                format_func=lambda value: "Keine Kategorie" if value == "" else value,
            )
            submitted = st.form_submit_button("Artikel speichern")

        if submitted:
            if item_name.strip():
                update_item(item["id"], item_name, quantity, category)
                st.success("Artikel wurde aktualisiert.")
                st.rerun()
            else:
                st.warning("Der Artikelname darf nicht leer sein.")

        if st.button("Artikel loeschen", key=f"delete-item-{item['id']}"):
            delete_item(item["id"])
            st.success("Artikel wurde geloescht.")
            st.rerun()


def render_items(user: dict, list_id: int) -> None:
    shopping_list = get_list_for_user(user["id"], list_id)
    if not shopping_list:
        st.warning("Diese Liste gehoert nicht zu deinem Account.")
        return

    st.divider()
    st.header(shopping_list["name"])
    render_list_actions(user, list_id, shopping_list["name"])

    with st.form("new-item-form", clear_on_submit=True):
        col_name, col_quantity = st.columns([2, 1])
        item_name = col_name.text_input("Artikel", placeholder="z. B. Milch")
        quantity = col_quantity.text_input("Menge", placeholder="z. B. 2 l")
        category = st.selectbox(
            "Kategorie",
            options=[""] + CATEGORIES,
            format_func=lambda value: "Keine Kategorie" if value == "" else value,
        )
        submitted = st.form_submit_button("Artikel hinzufuegen")

    if submitted:
        if item_name.strip():
            add_item(list_id, item_name, quantity, category)
            st.success("Artikel hinzugefuegt.")
            st.rerun()
        else:
            st.warning("Bitte gib einen Artikelnamen ein.")

    items = get_items(list_id)
    filter_choice = st.radio(
        "Artikel filtern",
        ["Alle", "Offen", "Erledigt"],
        horizontal=True,
    )
    visible_items = [
        item
        for item in items
        if filter_choice == "Alle"
        or (filter_choice == "Offen" and not item["is_done"])
        or (filter_choice == "Erledigt" and item["is_done"])
    ]
    open_items = [item for item in items if not item["is_done"]]
    done_items = [item for item in items if item["is_done"]]

    stat_cols = st.columns(3)
    stat_cols[0].metric("Offen", len(open_items))
    stat_cols[1].metric("Erledigt", len(done_items))
    stat_cols[2].metric("Gesamt", len(items))

    st.subheader("Artikel")
    if not visible_items:
        st.info("Keine Artikel fuer diesen Filter.")
    for item in visible_items:
        checked = st.checkbox(item_label(item), value=bool(item["is_done"]), key=f"item-{item['id']}")
        if checked != bool(item["is_done"]):
            set_item_done(item["id"], checked)
            st.rerun()
        render_item_editor(item)


def main() -> None:
    user = get_current_user()
    if not user:
        render_auth()
        return

    render_sidebar(user)
    st.title("Einkauf planen")
    st.caption("Sprint 2: Listen und Artikel bearbeiten, loeschen, kategorisieren und filtern.")
    lists = render_list_selector(user)
    active_list_id = st.session_state.get("active_list_id")
    if lists and active_list_id:
        render_items(user, active_list_id)


if __name__ == "__main__":
    main()
