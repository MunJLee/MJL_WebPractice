"""
This module is the entry point of this application.
RestApi endpoints are set here.

Created with Python 3.6.
See requirements.txt for dependencies.
"""

from flask import Flask, jsonify, render_template
import appserver

app = Flask(__name__)


@app.route("/")
def getIndex():
    #this brings up the rest api test page
    return render_template('index.html')


@app.route("/members", methods=["GET"])
def getAllRecords():
    return jsonify(appserver.getAllRecord())


@app.route("/members/<int:recordId>", methods=["GET"])
def getSingleRecord(recordId):
    result = appserver.getRecordWithID(recordId)

    if result is None:
        return jsonify({"error": "No Record"})
    else:
        return jsonify(result)


@app.route("/members/<int:recordId>/overdue", methods=["GET"])
def getAllOverdueEntries(recordId):
    return jsonify(appserver.getAllEntries(recordId, "overdue"))


@app.route("/members/<int:recordId>/overdue/<int:entryId>", methods=["GET"])
def getSingleOverdueEntry(recordId, entryId):
    result = appserver.getEntryWithID(recordId, "overdue", entryId)

    if result is None:
        return jsonify({"error": "No Entry"})
    else:
        return jsonify(result)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
