import pytest
import os
import tempfile
import yaml
from unittest.mock import patch, MagicMock
from src.detection_test_script import main

# Secure test constants - never use real API keys in tests
TEST_API_KEY = "test_api_key_for_testing_purposes_only_12345"


class TestIntegration:
    """Integration tests for the Detection AI Script."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.config_file = os.path.join(self.temp_dir, "integration_config.yml")
        
        # Create a test config file
        test_config = {
            "subject": "artificial intelligence",
            "tone": "educational and informative",
            "length": "150 words"
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
    def test_full_integration_flow(self, mock_exit, mock_model_class, mock_configure):
        """Test the complete integration flow from config to response."""
        # Mock the model and response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Artificial Intelligence (AI) represents a revolutionary field in computer science..."
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        # Set environment variable
        os.environ['GEMINI_API_KEY'] = TEST_API_KEY
        
        # Mock sys.argv
        with patch('sys.argv', ['script', '--yaml-file', self.config_file]):
            main()
        
        # Verify the complete flow
        mock_configure.assert_called_once()
        mock_model_class.assert_called_once_with('gemini-1.5-flash')
        mock_model.generate_content.assert_called_once()
        
        # Verify the prompt was constructed correctly
        call_args = mock_model.generate_content.call_args[0][0]
        assert "artificial intelligence" in call_args
        assert "educational and informative" in call_args
        assert "150 words" in call_args
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.genai.GenerativeModel')
    @patch('src.detection_test_script.sys.exit')
    def test_integration_with_custom_model(self, mock_exit, mock_model_class, mock_configure):
        """Test integration with a custom Gemini model."""
        # Mock the model and response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Custom model response..."
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        # Set environment variable
        os.environ['GEMINI_API_KEY'] = TEST_API_KEY
        
        # Mock sys.argv with custom model
        with patch('sys.argv', ['script', '--yaml-file', self.config_file, '--model', 'gemini-1.5-pro']):
            main()
        
        # Verify custom model was used
        mock_model_class.assert_called_once_with('gemini-1.5-pro')
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.genai.GenerativeModel')
    @patch('src.detection_test_script.sys.exit')
    def test_integration_with_api_key_argument(self, mock_exit, mock_model_class, mock_configure):
        """Test integration with API key passed as command line argument."""
        # Mock the model and response
        mock_model = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "API key argument response..."
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        # Remove environment variable
        os.environ.pop('GEMINI_API_KEY', None)
        
        # Mock sys.argv with API key argument
        with patch('sys.argv', ['script', '--yaml-file', self.config_file, '--api-key', TEST_API_KEY]):
            main()
        
        # Verify API key was used
        mock_configure.assert_called_once()
        mock_model_class.assert_called_once_with('gemini-1.5-flash')
    
    def test_config_file_parsing_integration(self):
        """Test that the config file is properly parsed and integrated."""
        # Read the config file
        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        # Verify all required fields are present
        assert 'subject' in config
        assert 'tone' in config
        assert 'length' in config
        
        # Verify field values
        assert config['subject'] == 'artificial intelligence'
        assert config['tone'] == 'educational and informative'
        assert config['length'] == '150 words'
    
    def test_environment_variable_integration(self):
        """Test environment variable integration."""
        # Set test environment variable
        test_key = TEST_API_KEY
        os.environ['GEMINI_API_KEY'] = test_key
        
        # Verify environment variable is set
        assert os.environ.get('GEMINI_API_KEY') == test_key
        
        # Clean up
        os.environ.pop('GEMINI_API_KEY', None)
    
    @patch('src.detection_test_script.genai.configure')
    @patch('src.detection_test_script.genai.GenerativeModel')
    @patch('src.detection_test_script.sys.exit')
    def test_error_handling_integration(self, mock_exit, mock_model_class, mock_configure):
        """Test error handling integration."""
        # Mock genai.configure to raise an exception
        mock_configure.side_effect = Exception("Integration test error")
        
        # Set environment variable
        os.environ['GEMINI_API_KEY'] = TEST_API_KEY
        
        # Mock sys.argv
        with patch('sys.argv', ['script', '--yaml-file', self.config_file]):
            main()
        
        # Verify error handling worked
        mock_exit.assert_called_once_with(1)


if __name__ == "__main__":
    pytest.main([__file__])
