# India States Quiz Game

A geographical quiz game built using Python and the **Turtle Graphics** library. The game challenges players to name all the states and union territories of India by clicking on a map and typing their names.

## 🚀 Features
* **Interactive Map:** A custom-styled map of India.
* **Real-time Scoring:** Tracks how many states you've guessed correctly.
* **Educational:** Helps users learn the locations of Indian states.
* **Data-Driven:** State names and coordinates are managed via a `CSV` file for easy updates.
* **Exit Strategy:** Type "Exit" at any time to save your progress or quit.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/india-states-quiz.git
    cd india-states-quiz
    ```

2.  **Ensure you have Python installed:**
    This project requires Python 3.x.

3.  **Required Libraries:**
    The project uses the standard `turtle`, `pandas`, and `csv` libraries. You can install Pandas via pip:
    ```bash
    pip install pandas
    ```

4.  **Image Files:**
    Ensure `India-states.gif` is in the root directory. Note that the Turtle library requires the '.gif' format for background images.

## 🎮 How to Play

1.  Run the `main.py` file:
    ```bash
    python main.py
    ```
2.  A window will open showing the map of India.
3.  Type the name of a state in the pop-up text box.
4.  If the name is correct:
    * The state name will appear at its correct $(x, y)$ coordinate on the map.
    * Your score will increase.
5.  Try to get all 28 states and 8 union territories!

## 📂 Project Structure
* `main.py`: The core game logic and Turtle screen management.
* `India-states.gif`: The background map image (Resized to fit portrait view).
* `india_coordinates.csv`: Contains the `state`, `x`, and `y` columns used to place text on the map.
* `states_to_learn.csv`: Generated if you exit early, showing you which states you missed.

## 🧪 Technical Implementation Details

### The Coordinate System
Because the map is a static image, we used a custom coordinate script to map the exact pixel locations of each state. 
* **Center of Screen:** $(0, 0)$
* **X-Range:** Approx -662 to +662
* **Y-Range:** Approx -768 to +768 (Portrait View)

### Image Scaling
The map image was optimized to **1324 x 1536** (or your specific resized dimensions) to ensure it fits within the standard Turtle canvas while maintaining legibility of state borders.

---

**Developed with by Vengat**
