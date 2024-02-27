import os
import requests

# Step 1: Download translate.py if not already present
translate_url = "https://raw.githubusercontent.com/ryzhkin/patches/main/translate.py"
translate_py_path = '/content/Fooocus/translate.py'  # Adjust path as necessary

if not os.path.exists(translate_py_path):
    r = requests.get(translate_url)
    with open(translate_py_path, 'w') as f:
        f.write(r.text)

# Step 2: Check if patch is already applied
webui_path = 'webui.py'  # Path to webui.py in Fooocus project
patch_signature = "from translate import isEnglish, translate"  # A unique line in your patch


def is_patch_applied(file_path, signature):
    with open(file_path, 'r') as file:
        if signature in file.read():
            return True
        else:
            return False


# Step 3: Apply the patch if not applied
if not is_patch_applied(webui_path, patch_signature):
    with open(webui_path, 'r') as file:
        content = file.readlines()

    # Find the index to insert your patch after the definition of generate_clicked
    insert_index = next(i for i, line in enumerate(content) if 'def generate_clicked(*args):' in line) + 1
    patch_lines = [
        "\n",
        "    from translate import isEnglish, translate\n",
        "    args_list = list(args)\n",
        "    if args_list and not isEnglish(args_list[0]):\n",
        "      args_list[0] = translate(args_list[0], 'en')\n",
        "      args = tuple(args_list)\n"
    ]
    for line in reversed(patch_lines):
        content.insert(insert_index, line)

    with open(webui_path, 'w') as file:
        file.writelines(content)
    print("Patch applied successfully.")
else:
    print("Patch is already applied.")
