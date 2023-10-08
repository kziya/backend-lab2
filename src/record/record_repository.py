from src.record.record_entity import Record


class RecordRepository:
    _records = []

    def addRecord(self, idUser, idCategory, expenditureAmount):
        if not self._records:
            record = Record(1, idUser, idCategory, expenditureAmount).getDict()
            self._records.append(record)
            return record
        else:
            lastElemId = self._records[-1].get('id')
            record = Record(lastElemId + 1, idUser, idCategory, expenditureAmount).getDict()
            self._records.append(record)
            return record

    def removeRecordById(self, id):
        targetRecordIndex = self._getIndexByRecordId(id)
        if targetRecordIndex is not None:
            self._records.pop(targetRecordIndex)
            return True
        else:
            return False

    def getRecordById(self, id):
        targetRecordIndex = self._getIndexByRecordId(id)
        if targetRecordIndex is not None:
            return self._records[targetRecordIndex]
        else:
            return None

    def getRecords(self, idUser, idCategory):
        filteredRecords = []
        for record in self._records:
            if (idUser is None or record.get('idUser') == idUser) and (
                    idCategory is None or record.get('idCategory') == idCategory):
                filteredRecords.append(record)

        return filteredRecords

    def _getIndexByRecordId(self, id):
        targetRecordIndex = None
        for index, record in enumerate(self._records):
            if record.get('id') == id:
                targetRecordIndex = index
                break
        print(id, targetRecordIndex)
        return targetRecordIndex


recordRepository = RecordRepository()
