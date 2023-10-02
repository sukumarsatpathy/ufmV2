import logging
from settings.models import WebSettings

logger = logging.getLogger(__name__)


def webSettingsUnivarsal(request):
    context = {
        'webSettingsUniversal': '',
    }
    try:
        webSettingsUniversal = WebSettings.objects.first()
        # if not webSettingsUniversal:
        #     raise ValueError("No settings available in the WebsiteSettings table.")

        context.update({
            'webSettingsUniversal': webSettingsUniversal,
        })

    except webSettingsUniversal.DoesNotExist:
        logger.warning("WebsiteSettings does not exist. Using default settings.")
        return {'webSettingsUniversal': ''}

    except AttributeError as e:
        logger.error(f"An attribute error occurred: {e}. Using default settings for the missing attributes.")
        return {'webSettingsUniversal': ''}

    except ValueError as e:
        logger.error(f"ValueError: {e}. Using default settings.")
        return {'webSettingsUniversal': ''}

    except Exception as e:
        logger.critical(f"Unexpected error occurred when fetching site settings: {e}. Using default settings.")
        return {'webSettingsUniversal': ''}

    return context