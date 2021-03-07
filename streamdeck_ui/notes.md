# TODO

## Module loader

* Seperate each action into a plugin.
* Figure out best how to contain this.
  * `actions/*` folder with sub folder for each action
  * Each folder will contain
    * A 24x24 icon for the tree view
    * One or more larger icons for the button
    * A module that is dynamically loaded
    * A class that adheres to a specific interface
### Interface
  * `GetUI(global_settings, action_settings)` A method that will return the UI, given settings (could be empty)
  * `global_settings` is settings for this Stream Deck that is global
  * `action_settings` is settings specific to this action (i.e. unique for each button)
  * Settings is a dictionary
  * `SaveSettings(global_settings, action_settings)` Call this method to save settings
  * `Run()` action is being run

## Drag and drop improvement
``` python
 def mouseMoveEvent(self, event):

        """Reimplement how to handle the widget being dragged. Change the mouse icon when the user begins dragging the object."""
        drag = QDrag(self)
        # When the user begins dragging the object, change the cursor's icon and set the drop action
        drag.setDragCursor(QPixmap("images/drag.png"), Qt.MoveAction)
        mime_data = QMimeData()
        drag.setMimeData(mime_data)
        # Create the QPainter object that will draw the widget being dragged
        pixmap = QPixmap(self.size()) # Get the size of the object
        painter = QPainter(pixmap) # Set the painter's pixmap
        # Draw the pixmap; grab() renders the widget into a pixmap specified by rect()
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap) # Set the pixmap to represent the drag action
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.MoveAction)
```

