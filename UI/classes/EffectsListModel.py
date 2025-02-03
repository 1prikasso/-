from PyQt5.QtCore import Qt, QAbstractListModel

class EffectsListModel(QAbstractListModel):
    def __init__(self, effects_objects=None, parent=None):
        super().__init__(parent)
        self.effects_objects = effects_objects or []

    def rowCount(self, parent=None):
        return len(self.effects_objects)

    def data(self, index, role):
        if not index.isValid():
            return None

        effect_object = self.effects_objects[index.row()]

        if role == Qt.DisplayRole:
            return effect_object.name

        return None

    def appendRow(self, item):
        self.beginInsertRows(self.createIndex(len(self.effects_objects), 0), len(self.effects_objects), len(self.effects_objects))
        self.effects_objects.append(item)
        self.endInsertRows()
