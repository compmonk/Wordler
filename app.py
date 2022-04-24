from flask import Flask, jsonify, request

from models import SearchConstraint, WordleTrie

app = Flask(__name__)

with open("wordle.txt") as wordle_file:
    wordle_trie = WordleTrie(map(lambda x: x.strip(), wordle_file.readlines()))


@app.route("/api/wordle", methods=["GET", "POST"])
def wordle():
    search_constraints = SearchConstraint.from_dicts(request.json)
    results = wordle_trie.search(search_constraints)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
