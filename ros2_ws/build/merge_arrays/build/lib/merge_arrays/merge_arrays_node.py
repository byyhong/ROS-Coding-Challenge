import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MergeArraysNode(Node):
    def __init__(self):
        super().__init__('merge_arrays_node')
        
        # Define Subscriber 1
        self.array1_sub = self.create_subscription(
            Int32MultiArray,
            '/input/array1',
            self.topic_callback,
            10
        )
        self.array1_sub
        # Define Subscriber 2
        self.array2_sub = self.create_subscription(
            Int32MultiArray,
            '/input/array2',
            self.topic_callback,
            10
        )
        self.array2_sub
        
        # Define the publisher
        self.merged_array_pub = self.create_publisher(Int32MultiArray, '/output/array', 10)

        # Initialize the result merged array
        self.merged_array = Int32MultiArray()
        self.merged=False
    def arr_equal(self, arr1, arr2):
        
        if(len(list(arr1)) != len(list(arr2))):
            return False
        for i in range(len(arr1)):
            if(arr1[i] != arr2[i]):
                return False
        return True
    def topic_callback(self, msg):
        self.temp = Int32MultiArray()
        if not self.merged_array.data:
            #Not received two data yet
            self.merged_array.data = msg.data
            self.temp = msg.data
    
        elif(not self.arr_equal(list(self.merged_array.data), list(msg.data)) and (not self.merged)):
            # Merge arrays
            self.merged_array.data = self.merge_sorted_arrays(self.merged_array.data, msg.data)
            # Publish the merged array
            self.merged_array_pub.publish(self.merged_array)
            self.merged = True
            #self.get_logger().info(list(self.merged_array.data))
            print(self.merged_array)
            return
    def merge_sorted_arrays(self, arr1, arr2):
        # Merge two sorted arrays
        merged_arr = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged_arr.append(arr1[i])
                i += 1
            else:
                merged_arr.append(arr2[j])
                j += 1
        merged_arr += arr1[i:]
        merged_arr += arr2[j:]
        return merged_arr

def main(args=None):
    rclpy.init(args=args)
    node = MergeArraysNode()
    
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



