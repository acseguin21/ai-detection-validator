import pytest
import os
import tempfile
import yaml
from unittest.mock import patch, MagicMock
from src.detection_test_script import validate_api_key, main


class TestValidateAPIKey:
    """Test cases for API key validation."""
    
    def test_valid_api_key(self):
        """Test that a valid API key passes validation."""
        valid_key = "AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz"
        is_valid, message = validate_api_key(valid_key)
        assert is_valid is True
        assert message == "API key format is valid"
    
    def test_empty_api_key(self):
        """Test that an empty API key fails validation."""
        is_valid, message = validate_api_key("")
        assert is_valid is False
        assert message == "API key is required"
    
    def test_none_api_key(self):
        """Test that None API key fails validation."""
        is_valid, message = validate_api_key(None)
        assert is_valid is False
        assert message == "API key is required"
    
    def test_short_api_key(self):
        """Test that a short API key fails validation."""
        short_key = "AI123"
        is_valid, message = validate_api_key(short_key)
        assert is_valid is False
        assert message == "API key appears to be too short"
    
    def test_invalid_prefix(self):
        """Test that an API key without 'AI' prefix fails validation."""
        invalid_key = "GOOGLE1234567890abcdefghijklmnopqrstuvwxyz"
        is_valid, message = validate_api_key(invalid_key)
        assert is_valid is False
        assert message == "API key should start with 'AI'"


class TestMainFunction:
    """Test cases for the main function."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = os.path.join(self.temp_dir, "test_config.yml")
        
        # Create a test config file
        test_config = {
            "subject": "test subject",
            "tone": "professional",
            "length": "50 words"
        }
        with open(self.config_file, 'w') as f:
            yaml.dump(test_config, f)
    
    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.genai.GenerativeModel')
    @patch('src.detection_test_script.sys.exit')
    def test_main_with_valid_api_key(self, mock_exit, mock_model_class, mock_configure):
        """Test main function with valid API key."""
        # Mock the model and response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "This is a test response about test subject."
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        # Set environment variable
        os.environ['GEMINI_API_KEY'] = 'AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz'
        
        # Mock sys.argv
        with patch('sys.argv', ['script', '--yaml-file', self.config_file]):
            main()
        
        # Verify genai.configure was called
        mock_configure.assert_called_once()
        
        # Verify model was created and generate_content was called
        mock_model_class.assert_called_once_with('gemini-1.5-flash')
        mock_model.generate_content.assert_called_once()
    
    @patch('src.detection_test_script.sys.exit')
    def test_main_without_api_key(self, mock_exit):
        """Test main function without API key."""
        # Remove environment variable if it exists
        os.environ.pop('GEMINI_API_KEY', None)
        
        # Mock sys.argv
        with patch('sys.argv', ['script', '--yaml-file', self.config_file]):
            main()
        
        # Verify sys.exit was called
        mock_exit.assert_called_once_with(1)
    
    @patch('src.detection_test_script.sys.exit')
    def test_main_with_invalid_api_key(self, mock_exit):
        """Test main function with invalid API key."""
        # Set invalid API key
        os.environ['GEMINI_API_KEY'] = 'invalid-key'
        
        # Mock sys.argv
        with patch('sys.argv', ['script', '--yaml-file', self.config_file]):
            main()
        
        # Verify sys.exit was called
        mock_exit.assert_called_once_with(1)
    
    @patch('src.detection_test_script.sys.exit')
    def test_main_with_nonexistent_yaml_file(self, mock_exit):
        """Test main function with nonexistent YAML file."""
        # Set valid API key
        os.environ['GEMINI_API_KEY'] = 'AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz'
        
        # Mock sys.argv with nonexistent file
        with patch('sys.argv', ['script', '--yaml-file', 'nonexistent.yml']):
            main()
        
        # Verify sys.exit was called
        mock_exit.assert_called_once_with(1)
    
    @patch('src.detection_test_script.sys.exit')
    def test_main_with_invalid_yaml_file(self, mock_exit):
        """Test main function with invalid YAML file."""
        # Create invalid YAML file
        invalid_yaml_file = os.path.join(self.temp_dir, "invalid.yml")
        with open(invalid_yaml_file, 'w') as f:
            f.write("invalid: yaml: content: [")
        
        # Set valid API key
        os.environ['GEMINI_API_KEY'] = 'AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz'
        
        # Mock sys.argv
        with patch('sys.argv', ['script', '--yaml-file', invalid_yaml_file]):
            main()
        
        # Verify sys.exit was called
        mock_exit.assert_called_once_with(1)
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.genai.GenerativeModel')
    @patch('src.detection_test_script.sys.exit')
    def test_main_with_custom_model(self, mock_exit, mock_model_class, mock_configure):
        """Test main function with custom model."""
        # Mock the model and response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "This is a test response."
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        # Set environment variable
        os.environ['GEMINI_API_KEY'] = 'AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz'
        
        # Mock sys.argv with custom model
        with patch('sys.argv', ['script', '--yaml-file', self.config_file, '--model', 'gemini-1.5-pro']):
            main()
        
        # Verify model was created with custom model
        mock_model_class.assert_called_once_with('gemini-1.5-pro')
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.genai.GenerativeModel')
    @patch('src.detection_test_script.sys.exit')
    def test_main_with_api_key_argument(self, mock_exit, mock_model_class, mock_configure):
        """Test main function with API key as command line argument."""
        # Mock the model and response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "This is a test response."
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        # Remove environment variable
        os.environ.pop('GEMINI_API_KEY', None)
        
        # Mock sys.argv with API key argument
        with patch('sys.argv', ['script', '--yaml-file', self.config_file, '--api-key', 'AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz']):
            main()
        
        # Verify genai.configure was called
        mock_configure.assert_called_once()


class TestErrorHandling:
    """Test cases for error handling."""
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.sys.exit')
    def test_genai_configure_error(self, mock_exit, mock_configure):
        """Test error handling when genai.configure fails."""
        # Mock genai.configure to raise an exception
        mock_configure.side_effect = Exception("Configuration error")
        
        # Set environment variable
        os.environ['GEMINI_API_KEY'] = 'AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz'
        
        # Create temporary config file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump({"subject": "test", "tone": "neutral", "length": "short"}, f)
            config_file = f.name
        
        try:
            # Mock sys.argv
            with patch('sys.argv', ['script', '--yaml-file', config_file]):
                main()
            
            # Verify sys.exit was called
            mock_exit.assert_called_once_with(1)
        finally:
            # Clean up
            os.unlink(config_file)
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.genai.GenerativeModel')
    @patch('src.detection_test_script.sys.exit')
    def test_model_generation_error(self, mock_exit, mock_model_class, mock_configure):
        """Test error handling when model generation fails."""
        # Mock the model to raise an exception during generation
        mock_model = MagicMock()
        mock_model.generate_content.side_effect = Exception("Generation error")
        mock_model_class.return_value = mock_model
        
        # Set environment variable
        os.environ['GEMINI_API_KEY'] = 'AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz'
        
        # Create temporary config file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            yaml.dump({"subject": "test", "tone": "neutral", "length": "short"}, f)
            config_file = f.name
        
        try:
            # Mock sys.argv
            with patch('sys.argv', ['script', '--yaml-file', config_file]):
                main()
            
            # Verify sys.exit was called
            mock_exit.assert_called_once_with(1)
        finally:
            # Clean up
            os.unlink(config_file)


if __name__ == "__main__":
    pytest.main([__file__])
