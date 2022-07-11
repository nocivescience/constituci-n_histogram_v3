from cv2 import rectangle
from manim import *
class ConstHistScene(Scene):
    CONFIG={
        'axes_config':{
            'x_range':[0,3,1],
            'x_axis_config':{
                'unit_size':1.2,
            },
            'y_range':[0,100,10],
            'y_axis_config':{
                'unit_size':0.065,
                'include_numbers':True,    
            },
        },
    }
    def construct(self):
        number_list=[np.random.random()*10 for i in range(10)]
        number_tracker=ValueTracker(1)
        axes=self.get_axes_hist()
        rectangle=self.get_rectangle(axes)
        labels=self.get_hist_labels(axes)
        rectangle.add_updater(
            lambda t: self.set_rectangle(rectangle,number_tracker.get_value())
        )
        self.add(rectangle,axes,labels)
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
    def get_axes_hist(self):
        axes=Axes(**self.CONFIG['axes_config'])
        return axes
    def get_rectangle(self,axes):
        rectangles=VGroup()
        for i in range(self.CONFIG['axes_config']['x_range'][1]-1):
            rectangles.add(
                Rectangle(
                    width=2,
                    height=5,
                ).move_to(
                    axes.c2p(i+1,0),
                    DOWN
                )
            )
        return rectangles
    def set_rectangle(self,rectangle,scale):
        rectangle.stretch_to_fit_height(scale,about_edge=DOWN)
    def get_hist_labels(self,axes):
        labels=VGroup(Text('Apruebo'),Text('Rechazo'))
        for i in range(len(labels)):
            labels[i].next_to(
                axes.c2p(i+1,0),
                DOWN,
                buff=0.3
            ).scale(.8)
        return labels