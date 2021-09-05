import pytest
from config.handle_filepath import report_file_path

#执行所有
pytest.main(["--html="+ report_file_path])

#执行单个
# pytest.main(["--html="+ report_file_path])嗷嗷


