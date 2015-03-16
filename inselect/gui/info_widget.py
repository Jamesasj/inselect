import humanize

from PySide.QtCore import QLocale
from PySide.QtGui import QWidget, QFormLayout, QLabel, QSizePolicy

from inselect.lib.utils import utc_format_local_display

class InfoWidget(QWidget):
    """Shows information about the document and the scanned image
    """
    def __init__(self, parent=None):
        super(InfoWidget, self).__init__(parent)

        layout = QFormLayout()
        # layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        layout.addRow(QLabel('Document'))

        self._document_path = QLabel()
        layout.addRow('Name', self._document_path)

        self._created_by = QLabel()
        layout.addRow('Created by', self._created_by)

        self._created_on = QLabel()
        layout.addRow('Created on', self._created_on)

        self._last_saved_by = QLabel()
        layout.addRow('Last saved by', self._last_saved_by)

        self._last_saved_on = QLabel()
        layout.addRow('Last saved on', self._last_saved_on)

        layout.addRow(QLabel('Scanned image'))
        self._scanned_path = QLabel()
        layout.addRow('Name', self._scanned_path)

        self._scanned_size = QLabel()
        layout.addRow('Size', self._scanned_size)

        self._scanned_dimensions = QLabel()
        layout.addRow('Dimensions', self._scanned_dimensions)

        self.setLayout(layout)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

    def set_document(self, document):
        """Set s a new document
        """
        if document:
            self._document_path.setText(document.document_path.name)

            p = document.properties
            self._created_by.setText(p.get('Created by'))

            dt = p.get('Created on')
            self._created_on.setText(utc_format_local_display(dt) if dt else '')

            self._last_saved_by.setText(p.get('Saved by'))

            dt = p.get('Saved on')
            self._last_saved_on.setText(utc_format_local_display(dt) if dt else '')

            self._scanned_path.setText(document.scanned.path.name)
            self._scanned_size.setText(humanize.naturalsize(document.scanned.size_bytes))

            dim = '{0:,} x {1:,}'
            self._scanned_dimensions.setText(dim.format(*document.scanned.dimensions))
        else:
            self._document_path.setText('')
            self._created_by.setText('')
            self._created_on.setText('')
            self._last_saved_by.setText('')
            self._last_saved_on.setText('')
            self._scanned_path.setText('')
            self._scanned_size.setText('')
            self._scanned_dimensions.setText('')