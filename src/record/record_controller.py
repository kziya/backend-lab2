from flask import request

from src import app
from src.record.record_service import RecordService

recordService = RecordService()


@app.route('/record', methods=['POST'])
def addRecord():
    return recordService.addRecord(request.get_json())


@app.route('/record/<int:id>', methods=['GET'])
def getRecordById(id):
    return recordService.getRecordById(id)


@app.route('/record', methods=['GET'])
def getRecords():
    return recordService.getRecords(request.get_json())
