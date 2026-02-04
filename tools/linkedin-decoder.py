import os
import html
def main():
    input_dir_name = "public"
    input_file_name = "code.html"

    output_dir_name = "public"
    output_file_name = "code.json"


    input_file_path = os.path.join(input_dir_name,input_file_name)
    with open(input_file_path, "r") as input_file:
        input_file_content = input_file.read()

    input_file_content = code_decoder(text=input_file_content)

    output_file_path = os.path.join(output_dir_name,output_file_name)
    with open(output_file_path, "w+") as output_file:
        output_file.write(input_file_content)

def code_decoder(text:str) -> str:

    text = text.replace("&quoquot;","&quot;",)
    text = html.unescape(text)
    return text


if __name__ == "__main__":
    main()
