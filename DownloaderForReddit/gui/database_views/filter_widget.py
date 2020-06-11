from PyQt5.QtWidgets import QWidget, QLabel, QToolButton, QHBoxLayout, QVBoxLayout, QListWidgetItem, QFrame, QListView
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor

from DownloaderForReddit.guiresources.database_views.filter_widget_auto import Ui_FilterWidget
from DownloaderForReddit.utils import injector
from .filter_item import FilterItem


class FilterWidget(QWidget, Ui_FilterWidget):

    filter_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.settings_manager = injector.get_settings_manager()
        self.active = False
        self.filters = {}
        self.list_item_map = {}

        self.filter_input_widget.export_filter.connect(self.add_filter)

        self.filter_box_list_widget.setSpacing(12)
        self.filter_box_list_widget.setResizeMode(QListView.Adjust)

    def set_default_filters(self, *filters):
        for filter_tuple in filters:
            self.add_filter(FilterItem(*filter_tuple))

    def filter(self, model_name):
        return self.filter_download_filters(model_name)

    def filter_download_filters(self, filter_name):
        return [x.filter_tuple for x in filter(lambda x: x.model == filter_name, self.filters.values())]

    def add_filter(self, filter_item=None):
        widget = self.create_widget(**filter_item.widget_dict)
        self.filters[widget] = filter_item
        self.add_widget_to_list(widget)
        self.filter_changed.emit(filter_item.model)

    def add_widget_to_list(self, widget):
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        item.setBackground(QColor('#C8C8C8'))
        self.filter_box_list_widget.addItem(item)
        self.filter_box_list_widget.setItemWidget(item, widget)
        self.list_item_map[widget] = item

    def create_widget(self, **kwargs):
        filter_item_widget = QWidget()

        model_label = QLabel(kwargs.get('model', None))
        field_label = QLabel(kwargs.get('field', None))
        operator_label = QLabel(kwargs.get('operator', None))
        # space added to this label text because it's the only way I could get it to stop cutting off the end of text
        value_label = QLabel(str(kwargs.get('value', None)) + '   ')

        close_button = QToolButton()
        close_button.setText('X')
        close_button.clicked.connect(lambda: self.remove_filter(filter_item_widget))

        v_layout = QVBoxLayout()
        title_layout = QHBoxLayout()
        title_layout.addWidget(model_label)
        title_layout.addWidget(close_button)

        h_layout = QHBoxLayout()
        h_layout.addWidget(field_label)
        h_layout.addWidget(self.get_line())
        h_layout.addWidget(operator_label)
        h_layout.addWidget(self.get_line())
        h_layout.addWidget(value_label)

        v_layout.addItem(title_layout)
        v_layout.addItem(h_layout)
        h_layout.setSpacing(5)
        v_layout.setSpacing(2)

        filter_item_widget.setLayout(v_layout)
        return filter_item_widget

    def get_line(self):
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        return line

    def remove_filter(self, widget):
        f = self.filters[widget]
        del self.filters[widget]
        item = self.list_item_map[widget]
        row = self.filter_box_list_widget.row(item)
        self.filter_box_list_widget.takeItem(row)
        self.filter_changed.emit(f.model)

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
    #         self.add_filter()
