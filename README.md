# tg_mass_forward

A Telegram userbot that forwards messages from a source chat to a list of target users. It handles various types of messages including text, photos, videos, documents, and audio, and ensures proper forwarding based on the sender and message type.

## Introduction

The `tg_message_forwarder` script is designed to automatically forward messages from a source chat to a list of target users. It can handle different types of messages and ensures that messages are forwarded correctly based on whether they are forwarded messages or original messages from the bot owner.

## Features

- **Forwards Messages:** Automatically forwards messages from a source chat to specified target users.
- **Handles Various Message Types:** Supports text, photos, videos, documents, audio, and voice messages.
- **Sender-Based Logic:** Forwards messages differently based on whether they are from the bot owner or forwarded messages.

## How It Works

1. **Forwarding Messages:**  
   The bot listens for messages in the specified source chat and forwards them to the target users based on specific conditions.

2. **Handling Forwarded Messages:**  
   If a message is forwarded, it is forwarded to the target users as is.

3. **Handling Messages from Bot Owner:**  
   If a message is from the bot owner, it is sent directly to the target users without the original sender's information.

4. **Handling Other Messages:**  
   If a message is neither forwarded nor from the bot owner, it is forwarded to the target users with the original sender's information.

## Getting Started

### Prerequisites

To use this script, you need to have the following:

- Python 3.8 or higher
- A Telegram account
- API credentials from Telegram (API ID and API Hash)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Commonlist/tg_message_forwarder.git
    ```

2. **Install the Required Packages:**  
   Navigate to the project directory and install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Credentials:**  
   You need to set up your API credentials for Telegram. You can find the instructions for obtaining these credentials in the respective documentation of Telegram.

### Configuration

Update the script `tg_message_forwarder.py` with your API credentials and chat/user information:

    ```python
    api_id = "your_api_id"
    api_hash = "your_api_hash"
    my_username = "your_username"  # Your Telegram username
    source_chat_id = -100source_chat_id  # ID of your source chat
    target_usernames = [
        "buzz_lightyear", "woody_pride", "mr_potato_head", "rex_the_dinosaur",
        "slinky_dog", "hamm_piggy_bank", "bo_peep", "duke_caboom",
        "gabby_gabby", "forbidden_planet_robot"
    ]
    ```

### Running the Script

To start the script, simply run:

    ```bash
    python tg_message_forwarder.py
    ```

or

    ```bash
    nohup python tg_message_forwarder.py &
    ```

The script will start monitoring the source chat for any messages and forward them to the target users as specified.

## Example Usage

- **Step 1:** Send a message to the source chat.
- **Step 2:** The bot forwards the message to the specified target users based on the conditions.

## Troubleshooting

If you encounter any issues while using the script, here are some common troubleshooting steps:

- **Check API Credentials:** Ensure that your API ID and API Hash are correct.
- **Check Chat and User IDs:** Make sure the source chat ID and target usernames are correct.
- **Internet Connection:** Make sure your internet connection is stable.
- **Script Errors:** If there are any errors in the script, refer to the error message for more details and fix the mentioned issues.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

By using this script, you can automate the forwarding of messages from a source chat to multiple target users efficiently.
