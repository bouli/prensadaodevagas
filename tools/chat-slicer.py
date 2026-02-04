import os
from datetime import datetime, timedelta
def main():
    input_dir_name = "./chats"
    input_file_name = "_chat.txt"

    output_dir_name = "./ohmyscrapper_input"
    output_file_name = "sliced_chat.txt"

    ensure_dir(dir_path=input_dir_name)
    input_file_path = os.path.join(input_dir_name,input_file_name)
    if not os.path.exists(input_file_path):
        print("There is no `./chats/chat.txt` available.")
        return
    with open(input_file_path, "r") as input_file:
        input_file_content = input_file.read()

    input_file_content = split_text_by_date(text=input_file_content,days=-8)

    ensure_dir(dir_path=output_dir_name)
    output_file_path = os.path.join(output_dir_name,output_file_name)
    with open(output_file_path, "w+") as output_file:
        input_file_content = format_chat_history(text=input_file_content)
        output_file.write(input_file_content)

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

def format_chat_history(text:str) -> str:
    message_marker = "[__message__]"
    text = annonimize_messages(text,message_marker)

    messages = text.split(message_marker)
    messages_with_links = []
    for message in messages:
        if message.find("https://") >= 0:
            messages_with_links.append(message)
    text = message_marker + message_marker.join(messages_with_links)
    return text

def annonimize_messages(text:str, message_marker="[__message__]") -> str:
    #cleaning
    text = text.replace("‎","")
    text = text.replace("imagem ocultada","")

    text_lines = text.split("\n")
    for text_line_index, text_line in enumerate(text_lines):
        if text_line[:1] == '[' and text_line[21:22] == ']':
            text_lines[text_line_index] = message_marker + text_line[22:].split(":",1)[1]

    text = "\n".join(text_lines)
    return text
def split_text_by_date(text:str,days:int) -> str:
    date_from = datetime.now() + timedelta(days=days)
    date_from = date_from.strftime("%d/%m/%Y")
    splitter_string = f"[{date_from}"

    text = text.split(splitter_string,1)[1]
    text = splitter_string+text

    return text


if __name__ == "__main__":
    main()
