import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SpiralTurtle(Node):
    def __init__(self):
        super().__init__('spiral_turtle')
        self.publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.spiral_move)
        self.linear_speed = 0.5

    def spiral_move(self):
        msg = Twist()
        msg.linear.x = self.linear_speed
        msg.angular.z = 1.5
        self.linear_speed += 0.01  
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SpiralTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

