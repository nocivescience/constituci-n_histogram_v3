from cv2 import rectangle
from manim import *
class ConstHistScene(Scene):
    def construct(self):
        number_list=[np.random.random()*10 for i in range(100)]
        number_tracker=ValueTracker(1)
        rectangle=self.get_rectangle()
        rectangle.add_updater(
            lambda t: self.set_rectangle(rectangle,number_tracker.get_value())
        )
        self.add(rectangle)
        for value in number_list:
            anims=[
                ApplyMethod(
                    number_tracker.set_value,value,
                    rate_func=linear,
                    run_time=.1,
                )
            ]
            self.play(*anims)
        self.wait()
    def get_rectangle(self):
        rectangle=Rectangle()
        return rectangle
    def set_rectangle(self,rectangle,scale):
        rectangle.stretch_to_fit_height(scale)