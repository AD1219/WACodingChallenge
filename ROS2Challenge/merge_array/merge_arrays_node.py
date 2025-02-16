import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class merge_arrays_node(Node):
    def __init__(self):
        super().__init__('merge_arrays_node')
        
        self.subscription1 = self.create_subscription(
            Int32MultiArray,
            '/input/array1',
            self.callback_arr1,
            10
        )
        self.subscription2 = self.create_subscription(
            Int32MultiArray,
            '/input/array2',
            self.callback_arr2,
            10
        )
        
        self.publisher_ = self.create_publisher(Int32MultiArray, '/output/array', 10)
        
        self.arr1 = []
        self.arr2 = []
    
    def callback_arr1(self, msg):
        self.arr1 = msg.data
        self.merge_and_publish()
    
    def callback_arr2(self, msg):
        self.arr2 = msg.data
        self.merge_and_publish()
    
    def merge_arr(self):
        if self.arr1 and self.arr2:
            merged_array = sorted(self.arr1 + self.arr2)
            msg = Int32MultiArray()
            msg.data = merged_array
            self.publisher_.publish(msg)
            self.get_logger().info(f'{merged_array}')


def main(args=None):
    rclpy.init(args=args)
    node = merge_arrays_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
