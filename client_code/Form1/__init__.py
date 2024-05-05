from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media

class Form1(Form1Template):  # Now correctly extending from Form1Template
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Any additional initialization code can go here
        self.button_generate.set_event_handler('click', self.button_generate_click)

    def button_generate_click(self, **event_args):
        # This function is triggered when the button is clicked.
        # It calls the server function 'get_plots' which returns an image.
        try:
            image_media = anvil.server.call('get_plots')
            self.image_plot.source = image_media
            self.label_status.text = "Plot generated successfully."
        except Exception as e:
            self.label_status.text = f"Failed to generate plot: {str(e)}"

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass
