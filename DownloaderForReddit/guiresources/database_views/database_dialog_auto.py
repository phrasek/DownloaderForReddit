# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\ui_files\database_views\database_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DatabaseDialog(object):
    def setupUi(self, DatabaseDialog):
        DatabaseDialog.setObjectName("DatabaseDialog")
        DatabaseDialog.resize(1698, 981)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources\\ui_files\\database_views\\../../images/database_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DatabaseDialog.setWindowIcon(icon)
        DatabaseDialog.setStyleSheet("")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(DatabaseDialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.model_focus_group_box = QtWidgets.QGroupBox(DatabaseDialog)
        self.model_focus_group_box.setMinimumSize(QtCore.QSize(0, 61))
        self.model_focus_group_box.setObjectName("model_focus_group_box")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.model_focus_group_box)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.download_session_focus_radio = QtWidgets.QRadioButton(self.model_focus_group_box)
        self.download_session_focus_radio.setObjectName("download_session_focus_radio")
        self.horizontalLayout_2.addWidget(self.download_session_focus_radio)
        self.reddit_object_focus_radio = QtWidgets.QRadioButton(self.model_focus_group_box)
        self.reddit_object_focus_radio.setObjectName("reddit_object_focus_radio")
        self.horizontalLayout_2.addWidget(self.reddit_object_focus_radio)
        self.post_focus_radio = QtWidgets.QRadioButton(self.model_focus_group_box)
        self.post_focus_radio.setObjectName("post_focus_radio")
        self.horizontalLayout_2.addWidget(self.post_focus_radio)
        self.content_focus_radio = QtWidgets.QRadioButton(self.model_focus_group_box)
        self.content_focus_radio.setObjectName("content_focus_radio")
        self.horizontalLayout_2.addWidget(self.content_focus_radio)
        self.comment_focus_radio = QtWidgets.QRadioButton(self.model_focus_group_box)
        self.comment_focus_radio.setObjectName("comment_focus_radio")
        self.horizontalLayout_2.addWidget(self.comment_focus_radio)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_download_sessions_checkbox = QtWidgets.QCheckBox(self.model_focus_group_box)
        self.show_download_sessions_checkbox.setObjectName("show_download_sessions_checkbox")
        self.horizontalLayout.addWidget(self.show_download_sessions_checkbox)
        self.show_reddit_objects_checkbox = QtWidgets.QCheckBox(self.model_focus_group_box)
        self.show_reddit_objects_checkbox.setObjectName("show_reddit_objects_checkbox")
        self.horizontalLayout.addWidget(self.show_reddit_objects_checkbox)
        self.show_posts_checkbox = QtWidgets.QCheckBox(self.model_focus_group_box)
        self.show_posts_checkbox.setObjectName("show_posts_checkbox")
        self.horizontalLayout.addWidget(self.show_posts_checkbox)
        self.show_content_checkbox = QtWidgets.QCheckBox(self.model_focus_group_box)
        self.show_content_checkbox.setObjectName("show_content_checkbox")
        self.horizontalLayout.addWidget(self.show_content_checkbox)
        self.show_comments_checkbox = QtWidgets.QCheckBox(self.model_focus_group_box)
        self.show_comments_checkbox.setObjectName("show_comments_checkbox")
        self.horizontalLayout.addWidget(self.show_comments_checkbox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.filter_button = QtWidgets.QPushButton(self.model_focus_group_box)
        self.filter_button.setCheckable(True)
        self.filter_button.setObjectName("filter_button")
        self.horizontalLayout_4.addWidget(self.filter_button)
        self.horizontalLayout_5.addWidget(self.model_focus_group_box)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.splitter = QtWidgets.QSplitter(DatabaseDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.filter_widget = FilterWidget(self.splitter)
        self.filter_widget.setObjectName("filter_widget")
        self.download_session_widget = QtWidgets.QWidget(self.splitter)
        self.download_session_widget.setObjectName("download_session_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.download_session_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.download_session_sort_combo = QtWidgets.QComboBox(self.download_session_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_session_sort_combo.sizePolicy().hasHeightForWidth())
        self.download_session_sort_combo.setSizePolicy(sizePolicy)
        self.download_session_sort_combo.setObjectName("download_session_sort_combo")
        self.horizontalLayout_3.addWidget(self.download_session_sort_combo)
        self.download_session_desc_sort_checkbox = QtWidgets.QCheckBox(self.download_session_widget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.download_session_desc_sort_checkbox.setFont(font)
        self.download_session_desc_sort_checkbox.setObjectName("download_session_desc_sort_checkbox")
        self.horizontalLayout_3.addWidget(self.download_session_desc_sort_checkbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.download_session_list_view = QtWidgets.QListView(self.download_session_widget)
        self.download_session_list_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.download_session_list_view.setObjectName("download_session_list_view")
        self.verticalLayout.addWidget(self.download_session_list_view)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.download_session_visible_count_label = QtWidgets.QLabel(self.download_session_widget)
        self.download_session_visible_count_label.setObjectName("download_session_visible_count_label")
        self.horizontalLayout_10.addWidget(self.download_session_visible_count_label)
        self.label_6 = QtWidgets.QLabel(self.download_session_widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.download_session_count_label = QtWidgets.QLabel(self.download_session_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_session_count_label.sizePolicy().hasHeightForWidth())
        self.download_session_count_label.setSizePolicy(sizePolicy)
        self.download_session_count_label.setObjectName("download_session_count_label")
        self.horizontalLayout_10.addWidget(self.download_session_count_label)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.load_more_download_sessions_button = QtWidgets.QPushButton(self.download_session_widget)
        self.load_more_download_sessions_button.setObjectName("load_more_download_sessions_button")
        self.verticalLayout.addWidget(self.load_more_download_sessions_button)
        self.reddit_object_widget = QtWidgets.QWidget(self.splitter)
        self.reddit_object_widget.setObjectName("reddit_object_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.reddit_object_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.reddit_object_sort_combo = QtWidgets.QComboBox(self.reddit_object_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reddit_object_sort_combo.sizePolicy().hasHeightForWidth())
        self.reddit_object_sort_combo.setSizePolicy(sizePolicy)
        self.reddit_object_sort_combo.setObjectName("reddit_object_sort_combo")
        self.horizontalLayout_6.addWidget(self.reddit_object_sort_combo)
        self.reddit_object_desc_sort_checkbox = QtWidgets.QCheckBox(self.reddit_object_widget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.reddit_object_desc_sort_checkbox.setFont(font)
        self.reddit_object_desc_sort_checkbox.setObjectName("reddit_object_desc_sort_checkbox")
        self.horizontalLayout_6.addWidget(self.reddit_object_desc_sort_checkbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.reddit_object_list_view = QtWidgets.QListView(self.reddit_object_widget)
        self.reddit_object_list_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reddit_object_list_view.setObjectName("reddit_object_list_view")
        self.verticalLayout_2.addWidget(self.reddit_object_list_view)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.reddit_object_visible_count_label = QtWidgets.QLabel(self.reddit_object_widget)
        self.reddit_object_visible_count_label.setObjectName("reddit_object_visible_count_label")
        self.horizontalLayout_11.addWidget(self.reddit_object_visible_count_label)
        self.label_2 = QtWidgets.QLabel(self.reddit_object_widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        self.reddit_object_count_label = QtWidgets.QLabel(self.reddit_object_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reddit_object_count_label.sizePolicy().hasHeightForWidth())
        self.reddit_object_count_label.setSizePolicy(sizePolicy)
        self.reddit_object_count_label.setObjectName("reddit_object_count_label")
        self.horizontalLayout_11.addWidget(self.reddit_object_count_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.load_more_reddit_objects_button = QtWidgets.QPushButton(self.reddit_object_widget)
        self.load_more_reddit_objects_button.setObjectName("load_more_reddit_objects_button")
        self.verticalLayout_2.addWidget(self.load_more_reddit_objects_button)
        self.post_widget = QtWidgets.QWidget(self.splitter)
        self.post_widget.setObjectName("post_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.post_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.post_sort_combo = QtWidgets.QComboBox(self.post_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.post_sort_combo.sizePolicy().hasHeightForWidth())
        self.post_sort_combo.setSizePolicy(sizePolicy)
        self.post_sort_combo.setObjectName("post_sort_combo")
        self.horizontalLayout_7.addWidget(self.post_sort_combo)
        self.post_desc_sort_checkbox = QtWidgets.QCheckBox(self.post_widget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.post_desc_sort_checkbox.setFont(font)
        self.post_desc_sort_checkbox.setObjectName("post_desc_sort_checkbox")
        self.horizontalLayout_7.addWidget(self.post_desc_sort_checkbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.post_text_splitter = QtWidgets.QSplitter(self.post_widget)
        self.post_text_splitter.setOrientation(QtCore.Qt.Vertical)
        self.post_text_splitter.setObjectName("post_text_splitter")
        self.post_table_view = QtWidgets.QTableView(self.post_text_splitter)
        self.post_table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.post_table_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.post_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.post_table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.post_table_view.setShowGrid(False)
        self.post_table_view.setGridStyle(QtCore.Qt.NoPen)
        self.post_table_view.setObjectName("post_table_view")
        self.post_table_view.horizontalHeader().setCascadingSectionResizes(False)
        self.post_text_browser = PostTextBrowser(self.post_text_splitter)
        self.post_text_browser.setOpenExternalLinks(True)
        self.post_text_browser.setObjectName("post_text_browser")
        self.verticalLayout_3.addWidget(self.post_text_splitter)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.post_visible_count_label = QtWidgets.QLabel(self.post_widget)
        self.post_visible_count_label.setObjectName("post_visible_count_label")
        self.horizontalLayout_12.addWidget(self.post_visible_count_label)
        self.label_3 = QtWidgets.QLabel(self.post_widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.post_count_label = QtWidgets.QLabel(self.post_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.post_count_label.sizePolicy().hasHeightForWidth())
        self.post_count_label.setSizePolicy(sizePolicy)
        self.post_count_label.setObjectName("post_count_label")
        self.horizontalLayout_12.addWidget(self.post_count_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.load_more_posts_button = QtWidgets.QPushButton(self.post_widget)
        self.load_more_posts_button.setObjectName("load_more_posts_button")
        self.verticalLayout_3.addWidget(self.load_more_posts_button)
        self.content_widget = QtWidgets.QWidget(self.splitter)
        self.content_widget.setObjectName("content_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.content_sort_combo = QtWidgets.QComboBox(self.content_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_sort_combo.sizePolicy().hasHeightForWidth())
        self.content_sort_combo.setSizePolicy(sizePolicy)
        self.content_sort_combo.setObjectName("content_sort_combo")
        self.horizontalLayout_8.addWidget(self.content_sort_combo)
        self.content_desc_sort_checkbox = QtWidgets.QCheckBox(self.content_widget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.content_desc_sort_checkbox.setFont(font)
        self.content_desc_sort_checkbox.setObjectName("content_desc_sort_checkbox")
        self.horizontalLayout_8.addWidget(self.content_desc_sort_checkbox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.content_list_view = QtWidgets.QListView(self.content_widget)
        self.content_list_view.setStyleSheet("")
        self.content_list_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.content_list_view.setIconSize(QtCore.QSize(0, 0))
        self.content_list_view.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.content_list_view.setFlow(QtWidgets.QListView.LeftToRight)
        self.content_list_view.setResizeMode(QtWidgets.QListView.Adjust)
        self.content_list_view.setLayoutMode(QtWidgets.QListView.Batched)
        self.content_list_view.setGridSize(QtCore.QSize(0, 0))
        self.content_list_view.setViewMode(QtWidgets.QListView.IconMode)
        self.content_list_view.setBatchSize(2)
        self.content_list_view.setWordWrap(True)
        self.content_list_view.setSelectionRectVisible(True)
        self.content_list_view.setObjectName("content_list_view")
        self.verticalLayout_4.addWidget(self.content_list_view)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(12)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.content_visible_count_label = QtWidgets.QLabel(self.content_widget)
        self.content_visible_count_label.setObjectName("content_visible_count_label")
        self.horizontalLayout_13.addWidget(self.content_visible_count_label)
        self.label_4 = QtWidgets.QLabel(self.content_widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_13.addWidget(self.label_4)
        self.content_count_label = QtWidgets.QLabel(self.content_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_count_label.sizePolicy().hasHeightForWidth())
        self.content_count_label.setSizePolicy(sizePolicy)
        self.content_count_label.setObjectName("content_count_label")
        self.horizontalLayout_13.addWidget(self.content_count_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.load_more_content_button = QtWidgets.QPushButton(self.content_widget)
        self.load_more_content_button.setObjectName("load_more_content_button")
        self.verticalLayout_4.addWidget(self.load_more_content_button)
        self.comment_widget = QtWidgets.QWidget(self.splitter)
        self.comment_widget.setObjectName("comment_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.comment_widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comment_sort_combo = QtWidgets.QComboBox(self.comment_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comment_sort_combo.sizePolicy().hasHeightForWidth())
        self.comment_sort_combo.setSizePolicy(sizePolicy)
        self.comment_sort_combo.setObjectName("comment_sort_combo")
        self.horizontalLayout_9.addWidget(self.comment_sort_combo)
        self.comment_desc_sort_checkbox = QtWidgets.QCheckBox(self.comment_widget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.comment_desc_sort_checkbox.setFont(font)
        self.comment_desc_sort_checkbox.setObjectName("comment_desc_sort_checkbox")
        self.horizontalLayout_9.addWidget(self.comment_desc_sort_checkbox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.comment_text_splitter = QtWidgets.QSplitter(self.comment_widget)
        self.comment_text_splitter.setOrientation(QtCore.Qt.Vertical)
        self.comment_text_splitter.setObjectName("comment_text_splitter")
        self.comment_tree_view = QtWidgets.QTreeView(self.comment_text_splitter)
        self.comment_tree_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.comment_tree_view.setObjectName("comment_tree_view")
        self.comment_text_browser = PostTextBrowser(self.comment_text_splitter)
        self.comment_text_browser.setObjectName("comment_text_browser")
        self.verticalLayout_7.addWidget(self.comment_text_splitter)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(12)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.comment_visible_count_label = QtWidgets.QLabel(self.comment_widget)
        self.comment_visible_count_label.setObjectName("comment_visible_count_label")
        self.horizontalLayout_14.addWidget(self.comment_visible_count_label)
        self.label_5 = QtWidgets.QLabel(self.comment_widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_14.addWidget(self.label_5)
        self.comment_count_label = QtWidgets.QLabel(self.comment_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comment_count_label.sizePolicy().hasHeightForWidth())
        self.comment_count_label.setSizePolicy(sizePolicy)
        self.comment_count_label.setObjectName("comment_count_label")
        self.horizontalLayout_14.addWidget(self.comment_count_label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.load_more_comments_button = QtWidgets.QPushButton(self.comment_widget)
        self.load_more_comments_button.setObjectName("load_more_comments_button")
        self.verticalLayout_7.addWidget(self.load_more_comments_button)
        self.verticalLayout_5.addWidget(self.splitter)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(DatabaseDialog)
        QtCore.QMetaObject.connectSlotsByName(DatabaseDialog)

    def retranslateUi(self, DatabaseDialog):
        _translate = QtCore.QCoreApplication.translate
        DatabaseDialog.setWindowTitle(_translate("DatabaseDialog", "Database"))
        self.model_focus_group_box.setTitle(_translate("DatabaseDialog", "Model Focus"))
        self.download_session_focus_radio.setText(_translate("DatabaseDialog", "Download Sessions"))
        self.reddit_object_focus_radio.setText(_translate("DatabaseDialog", "Reddit Objects"))
        self.post_focus_radio.setText(_translate("DatabaseDialog", "Posts"))
        self.content_focus_radio.setText(_translate("DatabaseDialog", "Content"))
        self.comment_focus_radio.setText(_translate("DatabaseDialog", "Comments"))
        self.show_download_sessions_checkbox.setText(_translate("DatabaseDialog", "Show download sessions"))
        self.show_reddit_objects_checkbox.setText(_translate("DatabaseDialog", "Show reddit objects"))
        self.show_posts_checkbox.setText(_translate("DatabaseDialog", "Show posts"))
        self.show_content_checkbox.setText(_translate("DatabaseDialog", "Show content"))
        self.show_comments_checkbox.setText(_translate("DatabaseDialog", "Show comments"))
        self.filter_button.setText(_translate("DatabaseDialog", "Filter"))
        self.download_session_desc_sort_checkbox.setText(_translate("DatabaseDialog", "desc."))
        self.download_session_visible_count_label.setText(_translate("DatabaseDialog", "0"))
        self.label_6.setText(_translate("DatabaseDialog", "of"))
        self.download_session_count_label.setText(_translate("DatabaseDialog", "0"))
        self.load_more_download_sessions_button.setText(_translate("DatabaseDialog", "Load More"))
        self.reddit_object_desc_sort_checkbox.setText(_translate("DatabaseDialog", "desc."))
        self.reddit_object_visible_count_label.setText(_translate("DatabaseDialog", "0"))
        self.label_2.setText(_translate("DatabaseDialog", "of"))
        self.reddit_object_count_label.setText(_translate("DatabaseDialog", "0"))
        self.load_more_reddit_objects_button.setText(_translate("DatabaseDialog", "Load More"))
        self.post_desc_sort_checkbox.setText(_translate("DatabaseDialog", "desc."))
        self.post_visible_count_label.setText(_translate("DatabaseDialog", "0"))
        self.label_3.setText(_translate("DatabaseDialog", "of"))
        self.post_count_label.setText(_translate("DatabaseDialog", "0"))
        self.load_more_posts_button.setText(_translate("DatabaseDialog", "Load More"))
        self.content_desc_sort_checkbox.setText(_translate("DatabaseDialog", "desc."))
        self.content_visible_count_label.setText(_translate("DatabaseDialog", "0"))
        self.label_4.setText(_translate("DatabaseDialog", "of"))
        self.content_count_label.setText(_translate("DatabaseDialog", "0"))
        self.load_more_content_button.setText(_translate("DatabaseDialog", "Load More"))
        self.comment_desc_sort_checkbox.setText(_translate("DatabaseDialog", "desc."))
        self.comment_visible_count_label.setText(_translate("DatabaseDialog", "0"))
        self.label_5.setText(_translate("DatabaseDialog", "of"))
        self.comment_count_label.setText(_translate("DatabaseDialog", "0"))
        self.load_more_comments_button.setText(_translate("DatabaseDialog", "Load More"))
from DownloaderForReddit.gui.database_views.filter_widget import FilterWidget
from DownloaderForReddit.gui.database_views.post_text_browser import PostTextBrowser
