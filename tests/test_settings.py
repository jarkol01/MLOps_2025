from settings import Settings


def test_settings_loading_with_valid_values():
    """Test that settings are loaded correctly with valid values."""
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "Test MLOps"
    assert settings.GOOGLE_API_KEY == ""
