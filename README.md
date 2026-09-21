# Playlist Manager

## Overview

Playlist Manager is a Python application built with Streamlit and a custom linked list data structure.

The application allows users to create and manage a music playlist while demonstrating how linked lists can be used in a real application.

## Features

The application allows users to:

* Add a track to the playlist
* Remove a track from the playlist
* Move to the next track
* Move to the previous track
* Reorder tracks in the playlist
* View the current playlist
* View the currently selected track

## Data Structure

The playlist is implemented using a custom linked list rather than relying on a standard Python list as the main playlist data structure.

Each track is stored inside a node.

Each node keeps references to neighboring tracks, allowing the application to move forward and backward through the playlist.

## Technologies Used

* Python
* Streamlit
* Custom Linked List
* GitHub
* Streamlit Community Cloud

## Project Structure

```text
Playlist-Manager/
├── app.py
├── linked_list.py
├── requirements.txt
├── README.md
└── AI_LOG.md
```

## Running the Application Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Live Application

The deployed Streamlit Community Cloud link will be added here after deployment.

**Live App:** Coming soon

## Development

This project is being developed through multiple meaningful Git commits to document the implementation process.

The development stages include:

1. Create the linked list structure
2. Implement adding and removing tracks
3. Implement next and previous track navigation
4. Implement playlist reordering
5. Build the Streamlit interface
6. Test and improve the application
7. Deploy the application to Streamlit Community Cloud

## Author

Younes Kouis
