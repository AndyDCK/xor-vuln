from flask import Flask, request, render_template
import base64

app = Flask(__name__)
KEY = b"secr3etkey"  # Faible, répétée pour XOR

def xor_encrypt(plaintext: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(plaintext)])

@app.route("/", methods=["GET", "POST"])
def index():
    token = ""
    decrypted = ""
    message = ""

    if request.method == "POST":
        if "get_token" in request.form:
            user = request.form["username"]
            plaintext = f"user:{user}".encode()
            ciphertext = xor_encrypt(plaintext, KEY)
            token = base64.urlsafe_b64encode(ciphertext).decode()

        elif "submit_token" in request.form:
            token = request.form["token"]
            try:
                decoded = base64.urlsafe_b64decode(token)
                decrypted = xor_encrypt(decoded, KEY).decode()
                if "admin" in decrypted:
                    message = "FLAG{broken_xor_auth}"
                else:
                    message = "Access denied."
            except Exception as e:
                message = f"Erreur : {e}"
    
    return render_template("index.html", token=token, decrypted=decrypted, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)