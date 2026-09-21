import streamlit as st
from linked_list import Playlist

st.set_page_config(page_title="Playlist Manager", page_icon="🎵")

st.title("🎵 Playlist Manager")

if "playlist" not in st.session_state:
    st.session_state.playlist = Playlist()

playlist = st.session_state.playlist


st.subheader("Add a Track")

track_name = st.text_input("Track name")

if st.button("Add Track"):
    if track_name.strip():
        playlist.add_track(track_name.strip())
        st.success(f"Added: {track_name}")
    else:
        st.warning("Enter a track name first.")


st.subheader("Current Track")

current_track = playlist.get_current_track()

if current_track:
    st.info(f"Now selected: {current_track}")
else:
    st.info("No track selected.")


col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Previous"):
        playlist.previous_track()

with col2:
    if st.button("Next ➡"):
        playlist.next_track()


st.subheader("Playlist")

tracks = playlist.get_tracks()

if not tracks:
    st.write("Your playlist is empty.")

else:
    for index, track in enumerate(tracks, start=1):
        st.write(f"{index}. {track}")


st.subheader("Manage Tracks")

if tracks:
    selected_track = st.selectbox(
        "Select a track",
        tracks
    )

    col3, col4, col5 = st.columns(3)

    with col3:
        if st.button("Remove"):
            playlist.remove_track(selected_track)
            st.rerun()

    with col4:
        if st.button("Move Up"):
            playlist.move_up(selected_track)
            st.rerun()

    with col5:
        if st.button("Move Down"):
            playlist.move_down(selected_track)
            st.rerun()
