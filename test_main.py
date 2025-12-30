import sys
from unittest.mock import Mock, patch, MagicMock
import pytest
from main import main, todo

@patch('main.QApplication')
def test_main_creates_qapplication(mock_qapp):
    mock_instance = MagicMock()
    mock_qapp.return_value = mock_instance
    
    with patch.object(mock_instance, 'exec_', side_effect=KeyboardInterrupt):
        try:
            main()
        except KeyboardInterrupt:
            pass
    
    mock_qapp.assert_called_once_with([])


@patch('main.todo')
@patch('main.QApplication')
def test_main_creates_todo_window(mock_qapp, mock_todo_class):
    mock_app_instance = MagicMock()
    mock_qapp.return_value = mock_app_instance
    mock_window_instance = MagicMock()
    mock_todo_class.return_value = mock_window_instance
    
    with patch.object(mock_app_instance, 'exec_', side_effect=KeyboardInterrupt):
        try:
            main()
        except KeyboardInterrupt:
            pass
    
    mock_todo_class.assert_called_once()


@patch('main.QApplication')
def test_main_calls_exec(mock_qapp):
    mock_instance = MagicMock()
    mock_qapp.return_value = mock_instance
    
    with patch.object(mock_instance, 'exec_', side_effect=KeyboardInterrupt):
        try:
            main()
        except KeyboardInterrupt:
            pass
    
    mock_instance.exec_.assert_called_once()