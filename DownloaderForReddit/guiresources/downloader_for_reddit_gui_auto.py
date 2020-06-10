# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Kyle/PycharmProjects/DownloaderForReddit/Resources/ui_files/downloader_for_reddit_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1232, 836)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Kyle/PycharmProjects/DownloaderForReddit/Resources/ui_files\\../Images/RedditDownloaderIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horz_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.horz_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.horz_splitter.setObjectName("horz_splitter")
        self.layoutWidget = QtWidgets.QWidget(self.horz_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.user_count_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_count_label.sizePolicy().hasHeightForWidth())
        self.user_count_label.setSizePolicy(sizePolicy)
        self.user_count_label.setObjectName("user_count_label")
        self.horizontalLayout_4.addWidget(self.user_count_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.user_list_search_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_list_search_edit.setObjectName("user_list_search_edit")
        self.verticalLayout.addWidget(self.user_list_search_edit)
        self.user_list_view = QtWidgets.QListView(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_list_view.setFont(font)
        self.user_list_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.user_list_view.setObjectName("user_list_view")
        self.verticalLayout.addWidget(self.user_list_view)
        self.user_lists_combo = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_lists_combo.setFont(font)
        self.user_lists_combo.setObjectName("user_lists_combo")
        self.verticalLayout.addWidget(self.user_lists_combo)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_user_button = QtWidgets.QPushButton(self.layoutWidget)
        self.add_user_button.setObjectName("add_user_button")
        self.horizontalLayout.addWidget(self.add_user_button)
        self.remove_user_button = QtWidgets.QPushButton(self.layoutWidget)
        self.remove_user_button.setObjectName("remove_user_button")
        self.horizontalLayout.addWidget(self.remove_user_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.horz_splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.subreddit_count_label = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subreddit_count_label.sizePolicy().hasHeightForWidth())
        self.subreddit_count_label.setSizePolicy(sizePolicy)
        self.subreddit_count_label.setObjectName("subreddit_count_label")
        self.horizontalLayout_5.addWidget(self.subreddit_count_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.subreddit_list_search_edit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.subreddit_list_search_edit.setObjectName("subreddit_list_search_edit")
        self.verticalLayout_2.addWidget(self.subreddit_list_search_edit)
        self.subreddit_list_view = QtWidgets.QListView(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subreddit_list_view.setFont(font)
        self.subreddit_list_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.subreddit_list_view.setObjectName("subreddit_list_view")
        self.verticalLayout_2.addWidget(self.subreddit_list_view)
        self.subreddit_list_combo = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subreddit_list_combo.setFont(font)
        self.subreddit_list_combo.setObjectName("subreddit_list_combo")
        self.verticalLayout_2.addWidget(self.subreddit_list_combo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_subreddit_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.add_subreddit_button.setObjectName("add_subreddit_button")
        self.horizontalLayout_2.addWidget(self.add_subreddit_button)
        self.remove_subreddit_button = QtWidgets.QPushButton(self.layoutWidget1)
        self.remove_subreddit_button.setObjectName("remove_subreddit_button")
        self.horizontalLayout_2.addWidget(self.remove_subreddit_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.horz_splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.download_button_layout = QtWidgets.QHBoxLayout()
        self.download_button_layout.setObjectName("download_button_layout")
        self.download_button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_button.setFont(font)
        self.download_button.setObjectName("download_button")
        self.download_button_layout.addWidget(self.download_button)
        self.soft_stop_download_button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.soft_stop_download_button.setFont(font)
        self.soft_stop_download_button.setObjectName("soft_stop_download_button")
        self.download_button_layout.addWidget(self.soft_stop_download_button)
        self.terminate_download_button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.terminate_download_button.setFont(font)
        self.terminate_download_button.setObjectName("terminate_download_button")
        self.download_button_layout.addWidget(self.terminate_download_button)
        self.verticalLayout_3.addLayout(self.download_button_layout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.download_users_radio = QtWidgets.QRadioButton(self.layoutWidget2)
        self.download_users_radio.setObjectName("download_users_radio")
        self.horizontalLayout_3.addWidget(self.download_users_radio)
        self.download_subreddits_radio = QtWidgets.QRadioButton(self.layoutWidget2)
        self.download_subreddits_radio.setObjectName("download_subreddits_radio")
        self.horizontalLayout_3.addWidget(self.download_subreddits_radio)
        self.constain_to_sub_list_radio = QtWidgets.QRadioButton(self.layoutWidget2)
        self.constain_to_sub_list_radio.setObjectName("constain_to_sub_list_radio")
        self.horizontalLayout_3.addWidget(self.constain_to_sub_list_radio)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.layoutWidget2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.schedule_widget = QtWidgets.QWidget(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_widget.sizePolicy().hasHeightForWidth())
        self.schedule_widget.setSizePolicy(sizePolicy)
        self.schedule_widget.setMaximumSize(QtCore.QSize(16777215, 15))
        self.schedule_widget.setObjectName("schedule_widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.schedule_widget)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.schedule_widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.schedule_label = QtWidgets.QLabel(self.schedule_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_label.sizePolicy().hasHeightForWidth())
        self.schedule_label.setSizePolicy(sizePolicy)
        self.schedule_label.setObjectName("schedule_label")
        self.horizontalLayout_8.addWidget(self.schedule_label)
        self.verticalLayout_3.addWidget(self.schedule_widget)
        self.output_box = QtWidgets.QTextBrowser(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_box.setFont(font)
        self.output_box.setObjectName("output_box")
        self.verticalLayout_3.addWidget(self.output_box)
        self.verticalLayout_4.addWidget(self.horz_splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1232, 31))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.lists_menu = QtWidgets.QMenu(self.menubar)
        self.lists_menu.setObjectName("lists_menu")
        self.export_user_list_menu = QtWidgets.QMenu(self.lists_menu)
        self.export_user_list_menu.setObjectName("export_user_list_menu")
        self.file_export_subreddit_list = QtWidgets.QMenu(self.lists_menu)
        self.file_export_subreddit_list.setObjectName("file_export_subreddit_list")
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        self.view_menu = QtWidgets.QMenu(self.menubar)
        self.view_menu.setObjectName("view_menu")
        self.list_sort_menu_item = QtWidgets.QMenu(self.view_menu)
        self.list_sort_menu_item.setObjectName("list_sort_menu_item")
        self.list_order_menu_item = QtWidgets.QMenu(self.view_menu)
        self.list_order_menu_item.setObjectName("list_order_menu_item")
        self.menuDownload = QtWidgets.QMenu(self.menubar)
        self.menuDownload.setObjectName("menuDownload")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.add_user_list_menu_item = QtWidgets.QAction(MainWindow)
        self.add_user_list_menu_item.setObjectName("add_user_list_menu_item")
        self.add_subreddit_list_menu_item = QtWidgets.QAction(MainWindow)
        self.add_subreddit_list_menu_item.setObjectName("add_subreddit_list_menu_item")
        self.file_save = QtWidgets.QAction(MainWindow)
        self.file_save.setObjectName("file_save")
        self.remove_user_list_menu_item = QtWidgets.QAction(MainWindow)
        self.remove_user_list_menu_item.setObjectName("remove_user_list_menu_item")
        self.remove_subreddit_list_menu_item = QtWidgets.QAction(MainWindow)
        self.remove_subreddit_list_menu_item.setObjectName("remove_subreddit_list_menu_item")
        self.open_settings_menu_item = QtWidgets.QAction(MainWindow)
        self.open_settings_menu_item.setObjectName("open_settings_menu_item")
        self.exit_menu_item = QtWidgets.QAction(MainWindow)
        self.exit_menu_item.setObjectName("exit_menu_item")
        self.failed_download_view_menu_item = QtWidgets.QAction(MainWindow)
        self.failed_download_view_menu_item.setObjectName("failed_download_view_menu_item")
        self.file_open_user_finder = QtWidgets.QAction(MainWindow)
        self.file_open_user_finder.setObjectName("file_open_user_finder")
        self.download_session_menu_item = QtWidgets.QAction(MainWindow)
        self.download_session_menu_item.setObjectName("download_session_menu_item")
        self.failed_extraction_view_menu_item = QtWidgets.QAction(MainWindow)
        self.failed_extraction_view_menu_item.setObjectName("failed_extraction_view_menu_item")
        self.imgur_credit_dialog_menu_item = QtWidgets.QAction(MainWindow)
        self.imgur_credit_dialog_menu_item.setObjectName("imgur_credit_dialog_menu_item")
        self.about_menu_item = QtWidgets.QAction(MainWindow)
        self.about_menu_item.setObjectName("about_menu_item")
        self.file_user_list_count = QtWidgets.QAction(MainWindow)
        self.file_user_list_count.setObjectName("file_user_list_count")
        self.file_subreddit_list_count = QtWidgets.QAction(MainWindow)
        self.file_subreddit_list_count.setObjectName("file_subreddit_list_count")
        self.user_manual_menu_item = QtWidgets.QAction(MainWindow)
        self.user_manual_menu_item.setObjectName("user_manual_menu_item")
        self.check_for_updates_menu_item = QtWidgets.QAction(MainWindow)
        self.check_for_updates_menu_item.setObjectName("check_for_updates_menu_item")
        self.sort_list_by_name_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_by_name_menu_item.setCheckable(True)
        self.sort_list_by_name_menu_item.setObjectName("sort_list_by_name_menu_item")
        self.sort_list_by_date_added_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_by_date_added_menu_item.setCheckable(True)
        self.sort_list_by_date_added_menu_item.setObjectName("sort_list_by_date_added_menu_item")
        self.sort_list_by_post_count_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_by_post_count_menu_item.setCheckable(True)
        self.sort_list_by_post_count_menu_item.setObjectName("sort_list_by_post_count_menu_item")
        self.sort_list_ascending_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_ascending_menu_item.setCheckable(True)
        self.sort_list_ascending_menu_item.setObjectName("sort_list_ascending_menu_item")
        self.sort_list_descending_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_descending_menu_item.setCheckable(True)
        self.sort_list_descending_menu_item.setObjectName("sort_list_descending_menu_item")
        self.open_data_directory_menu_item = QtWidgets.QAction(MainWindow)
        self.open_data_directory_menu_item.setObjectName("open_data_directory_menu_item")
        self.import_database_file_menu_item = QtWidgets.QAction(MainWindow)
        self.import_database_file_menu_item.setObjectName("import_database_file_menu_item")
        self.export_user_list_as_text_menu_item = QtWidgets.QAction(MainWindow)
        self.export_user_list_as_text_menu_item.setObjectName("export_user_list_as_text_menu_item")
        self.export_user_list_as_json_menu_item = QtWidgets.QAction(MainWindow)
        self.export_user_list_as_json_menu_item.setObjectName("export_user_list_as_json_menu_item")
        self.export_sub_list_as_text_menu_item = QtWidgets.QAction(MainWindow)
        self.export_sub_list_as_text_menu_item.setObjectName("export_sub_list_as_text_menu_item")
        self.export_sub_list_as_json_menu_item = QtWidgets.QAction(MainWindow)
        self.export_sub_list_as_json_menu_item.setObjectName("export_sub_list_as_json_menu_item")
        self.export_sub_list_as_xml_menu_item = QtWidgets.QAction(MainWindow)
        self.export_sub_list_as_xml_menu_item.setObjectName("export_sub_list_as_xml_menu_item")
        self.export_user_list_as_xml_menu_item = QtWidgets.QAction(MainWindow)
        self.export_user_list_as_xml_menu_item.setObjectName("export_user_list_as_xml_menu_item")
        self.ffmpeg_requirement_dialog_menu_item = QtWidgets.QAction(MainWindow)
        self.ffmpeg_requirement_dialog_menu_item.setObjectName("ffmpeg_requirement_dialog_menu_item")
        self.download_user_list_menu_item = QtWidgets.QAction(MainWindow)
        self.download_user_list_menu_item.setObjectName("download_user_list_menu_item")
        self.download_subreddit_list_menu_item = QtWidgets.QAction(MainWindow)
        self.download_subreddit_list_menu_item.setObjectName("download_subreddit_list_menu_item")
        self.download_user_list_constrained_menu_item = QtWidgets.QAction(MainWindow)
        self.download_user_list_constrained_menu_item.setObjectName("download_user_list_constrained_menu_item")
        self.run_unfinished_extractions_menu_item = QtWidgets.QAction(MainWindow)
        self.run_unfinished_extractions_menu_item.setObjectName("run_unfinished_extractions_menu_item")
        self.run_unfinished_downloads_menu_item = QtWidgets.QAction(MainWindow)
        self.run_unfinished_downloads_menu_item.setObjectName("run_unfinished_downloads_menu_item")
        self.sort_list_by_content_count_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_by_content_count_menu_item.setObjectName("sort_list_by_content_count_menu_item")
        self.sort_list_by_comment_count_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_by_comment_count_menu_item.setObjectName("sort_list_by_comment_count_menu_item")
        self.sort_list_by_date_created_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_by_date_created_menu_item.setObjectName("sort_list_by_date_created_menu_item")
        self.sort_list_by_score_menu_item = QtWidgets.QAction(MainWindow)
        self.sort_list_by_score_menu_item.setObjectName("sort_list_by_score_menu_item")
        self.database_view_menu_item = QtWidgets.QAction(MainWindow)
        self.database_view_menu_item.setObjectName("database_view_menu_item")
        self.download_sessions_view_menu_item = QtWidgets.QAction(MainWindow)
        self.download_sessions_view_menu_item.setObjectName("download_sessions_view_menu_item")
        self.reddit_objects_view_menu_item = QtWidgets.QAction(MainWindow)
        self.reddit_objects_view_menu_item.setObjectName("reddit_objects_view_menu_item")
        self.posts_view_menu_item = QtWidgets.QAction(MainWindow)
        self.posts_view_menu_item.setObjectName("posts_view_menu_item")
        self.content_view_menu_item = QtWidgets.QAction(MainWindow)
        self.content_view_menu_item.setObjectName("content_view_menu_item")
        self.comments_view_menu_item = QtWidgets.QAction(MainWindow)
        self.comments_view_menu_item.setObjectName("comments_view_menu_item")
        self.statistics_view_menu_item = QtWidgets.QAction(MainWindow)
        self.statistics_view_menu_item.setObjectName("statistics_view_menu_item")
        self.run_all_unfiinished_menu_item = QtWidgets.QAction(MainWindow)
        self.run_all_unfiinished_menu_item.setObjectName("run_all_unfiinished_menu_item")
        self.file_menu.addAction(self.open_settings_menu_item)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.open_data_directory_menu_item)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_menu_item)
        self.export_user_list_menu.addAction(self.export_user_list_as_text_menu_item)
        self.export_user_list_menu.addAction(self.export_user_list_as_json_menu_item)
        self.file_export_subreddit_list.addAction(self.export_sub_list_as_text_menu_item)
        self.file_export_subreddit_list.addAction(self.export_sub_list_as_json_menu_item)
        self.lists_menu.addAction(self.add_user_list_menu_item)
        self.lists_menu.addAction(self.add_subreddit_list_menu_item)
        self.lists_menu.addSeparator()
        self.lists_menu.addAction(self.remove_user_list_menu_item)
        self.lists_menu.addAction(self.remove_subreddit_list_menu_item)
        self.lists_menu.addSeparator()
        self.lists_menu.addAction(self.export_user_list_menu.menuAction())
        self.lists_menu.addAction(self.file_export_subreddit_list.menuAction())
        self.lists_menu.addSeparator()
        self.lists_menu.addSeparator()
        self.help_menu.addAction(self.imgur_credit_dialog_menu_item)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.user_manual_menu_item)
        self.help_menu.addAction(self.ffmpeg_requirement_dialog_menu_item)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.check_for_updates_menu_item)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.about_menu_item)
        self.list_order_menu_item.addAction(self.sort_list_ascending_menu_item)
        self.list_order_menu_item.addAction(self.sort_list_descending_menu_item)
        self.view_menu.addAction(self.list_sort_menu_item.menuAction())
        self.view_menu.addAction(self.list_order_menu_item.menuAction())
        self.menuDownload.addAction(self.download_user_list_menu_item)
        self.menuDownload.addAction(self.download_subreddit_list_menu_item)
        self.menuDownload.addAction(self.download_user_list_constrained_menu_item)
        self.menuDownload.addSeparator()
        self.menuDownload.addAction(self.run_unfinished_extractions_menu_item)
        self.menuDownload.addAction(self.run_unfinished_downloads_menu_item)
        self.menuDownload.addAction(self.run_all_unfiinished_menu_item)
        self.menuDatabase.addAction(self.database_view_menu_item)
        self.menuDatabase.addSeparator()
        self.menuDatabase.addAction(self.download_sessions_view_menu_item)
        self.menuDatabase.addAction(self.reddit_objects_view_menu_item)
        self.menuDatabase.addAction(self.posts_view_menu_item)
        self.menuDatabase.addAction(self.content_view_menu_item)
        self.menuDatabase.addAction(self.comments_view_menu_item)
        self.menuDatabase.addSeparator()
        self.menuDatabase.addAction(self.failed_extraction_view_menu_item)
        self.menuDatabase.addAction(self.failed_download_view_menu_item)
        self.menuDatabase.addSeparator()
        self.menuDatabase.addAction(self.statistics_view_menu_item)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.view_menu.menuAction())
        self.menubar.addAction(self.lists_menu.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuDownload.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloader for Reddit"))
        self.label_2.setText(_translate("MainWindow", "Users:"))
        self.user_count_label.setText(_translate("MainWindow", "0"))
        self.user_list_search_edit.setPlaceholderText(_translate("MainWindow", "Search users"))
        self.user_lists_combo.setToolTip(_translate("MainWindow", "Current user list"))
        self.add_user_button.setText(_translate("MainWindow", "Add User"))
        self.remove_user_button.setText(_translate("MainWindow", "Remove User"))
        self.label_4.setText(_translate("MainWindow", "Subreddits:"))
        self.subreddit_count_label.setText(_translate("MainWindow", "0"))
        self.subreddit_list_search_edit.setPlaceholderText(_translate("MainWindow", "Search subreddits"))
        self.subreddit_list_combo.setToolTip(_translate("MainWindow", "Current subreddit list"))
        self.add_subreddit_button.setText(_translate("MainWindow", "Add Subreddit"))
        self.remove_subreddit_button.setText(_translate("MainWindow", "Remove Subreddit"))
        self.download_button.setToolTip(_translate("MainWindow", "Download selected user or subreddit list"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.soft_stop_download_button.setToolTip(_translate("MainWindow", "Stops the current download, but allows in progress downloads to finish"))
        self.soft_stop_download_button.setText(_translate("MainWindow", "Stop Download"))
        self.terminate_download_button.setToolTip(_translate("MainWindow", "Stops the download immediately and terminates in progress downloads (may result in corrupted files for downloads that were not complete)"))
        self.terminate_download_button.setText(_translate("MainWindow", "Terminate Download"))
        self.download_users_radio.setToolTip(_translate("MainWindow", "Download only user list"))
        self.download_users_radio.setText(_translate("MainWindow", "Users"))
        self.download_subreddits_radio.setToolTip(_translate("MainWindow", "Download only subreddit list"))
        self.download_subreddits_radio.setText(_translate("MainWindow", "Subreddits"))
        self.constain_to_sub_list_radio.setToolTip(_translate("MainWindow", "<html><head/><body><p>Download user list, but only extract posts made to subreddits in the subreddit list</p></body></html>"))
        self.constain_to_sub_list_radio.setText(_translate("MainWindow", "Constrain Users To Subreddit List"))
        self.label_3.setText(_translate("MainWindow", "Download Scheduled:"))
        self.schedule_label.setText(_translate("MainWindow", "00:00:00"))
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.lists_menu.setTitle(_translate("MainWindow", "Lists"))
        self.export_user_list_menu.setTitle(_translate("MainWindow", "Export User List"))
        self.file_export_subreddit_list.setTitle(_translate("MainWindow", "Export Subreddit List"))
        self.help_menu.setTitle(_translate("MainWindow", "Help"))
        self.view_menu.setTitle(_translate("MainWindow", "View"))
        self.list_sort_menu_item.setTitle(_translate("MainWindow", "Sort Lists By"))
        self.list_order_menu_item.setTitle(_translate("MainWindow", "Sort Order"))
        self.menuDownload.setTitle(_translate("MainWindow", "Download"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.add_user_list_menu_item.setText(_translate("MainWindow", "Add User List"))
        self.add_subreddit_list_menu_item.setText(_translate("MainWindow", "Add Subreddit List"))
        self.file_save.setText(_translate("MainWindow", "Save"))
        self.remove_user_list_menu_item.setText(_translate("MainWindow", "Remove User List"))
        self.remove_subreddit_list_menu_item.setText(_translate("MainWindow", "Remove Subreddit List"))
        self.open_settings_menu_item.setText(_translate("MainWindow", "Settings"))
        self.exit_menu_item.setText(_translate("MainWindow", "Exit"))
        self.failed_download_view_menu_item.setText(_translate("MainWindow", "Failed Download"))
        self.failed_download_view_menu_item.setToolTip(_translate("MainWindow", "Display the failed download list for the last download session"))
        self.file_open_user_finder.setText(_translate("MainWindow", "Open User Finder"))
        self.download_session_menu_item.setText(_translate("MainWindow", "Download Sessions"))
        self.failed_extraction_view_menu_item.setText(_translate("MainWindow", "Failed Extractions"))
        self.imgur_credit_dialog_menu_item.setText(_translate("MainWindow", "Imgur Credits"))
        self.about_menu_item.setText(_translate("MainWindow", "About"))
        self.file_user_list_count.setText(_translate("MainWindow", "User List Count:"))
        self.file_subreddit_list_count.setText(_translate("MainWindow", "Subreddit List Count:"))
        self.user_manual_menu_item.setText(_translate("MainWindow", "User Manual"))
        self.check_for_updates_menu_item.setText(_translate("MainWindow", "Check For Update"))
        self.sort_list_by_name_menu_item.setText(_translate("MainWindow", "Name"))
        self.sort_list_by_date_added_menu_item.setText(_translate("MainWindow", "Date Added"))
        self.sort_list_by_post_count_menu_item.setText(_translate("MainWindow", "Post Count"))
        self.sort_list_ascending_menu_item.setText(_translate("MainWindow", "Ascending"))
        self.sort_list_descending_menu_item.setText(_translate("MainWindow", "Descending"))
        self.open_data_directory_menu_item.setText(_translate("MainWindow", "Open Data Directory"))
        self.import_database_file_menu_item.setText(_translate("MainWindow", "Import Save File"))
        self.export_user_list_as_text_menu_item.setText(_translate("MainWindow", "Export As Text"))
        self.export_user_list_as_json_menu_item.setText(_translate("MainWindow", "Export As Json"))
        self.export_sub_list_as_text_menu_item.setText(_translate("MainWindow", "Export As Text"))
        self.export_sub_list_as_json_menu_item.setText(_translate("MainWindow", "Export As Json"))
        self.export_sub_list_as_xml_menu_item.setText(_translate("MainWindow", "Export As Xml"))
        self.export_user_list_as_xml_menu_item.setText(_translate("MainWindow", "Export As Xml"))
        self.ffmpeg_requirement_dialog_menu_item.setText(_translate("MainWindow", "FFmpeg Requirement"))
        self.download_user_list_menu_item.setText(_translate("MainWindow", "Download User List"))
        self.download_subreddit_list_menu_item.setText(_translate("MainWindow", "Download Subreddit List"))
        self.download_user_list_constrained_menu_item.setText(_translate("MainWindow", "Download User List Constrained"))
        self.download_user_list_constrained_menu_item.setToolTip(_translate("MainWindow", "<html><head/><body><p>Download user list, but only extract posts made to subreddits in the subreddit list</p></body></html>"))
        self.run_unfinished_extractions_menu_item.setText(_translate("MainWindow", "Run Unfinished Extractions"))
        self.run_unfinished_downloads_menu_item.setText(_translate("MainWindow", "Run Unfinished Downloads"))
        self.sort_list_by_content_count_menu_item.setText(_translate("MainWindow", "Content Count"))
        self.sort_list_by_comment_count_menu_item.setText(_translate("MainWindow", "Comment Count"))
        self.sort_list_by_date_created_menu_item.setText(_translate("MainWindow", "Date Created"))
        self.sort_list_by_date_created_menu_item.setToolTip(_translate("MainWindow", "Sort reddit objects by the date that the item was created on reddit"))
        self.sort_list_by_score_menu_item.setText(_translate("MainWindow", "Total Score"))
        self.database_view_menu_item.setText(_translate("MainWindow", "Database View"))
        self.download_sessions_view_menu_item.setText(_translate("MainWindow", "Download Sessions"))
        self.reddit_objects_view_menu_item.setText(_translate("MainWindow", "Reddit Objects"))
        self.posts_view_menu_item.setText(_translate("MainWindow", "Posts"))
        self.content_view_menu_item.setText(_translate("MainWindow", "Content"))
        self.comments_view_menu_item.setText(_translate("MainWindow", "Comments"))
        self.statistics_view_menu_item.setText(_translate("MainWindow", "Statistics"))
        self.run_all_unfiinished_menu_item.setText(_translate("MainWindow", "Run All Unfinished"))
