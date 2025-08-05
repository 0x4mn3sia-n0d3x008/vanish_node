# Vanish Chat 💬🔥

A minimal, retro 90s-style vanish chat web app built with Flask & Socket.IO — anonymous usernames, timestamped messages, self-message highlights, and auto-vanishing messages after 45 seconds.

---

## Features

- Anonymous usernames like `{node_0xXXXX}`
- Real-time chat with Flask + Socket.IO
- Messages auto-delete 45 seconds after sending (vanish mode)
- Timestamped messages
- Self message highlighting
- Minimal 90s terminal-style UI
- Create or join chat rooms with secret room codes

---

## Getting Started

### Requirements

- Python 3.8+
- `pip` package manager

### Install & Run

```bash
git clone https://github.com/yourusername/vanish-chat.git
cd vanish-chat
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
