import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class RobotMotion(Node):

    def __init__(self):
        super().__init__('robot_motion')

        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.publish_tf)
        self.start_time = self.get_clock().now()

    def publish_tf(self):
        elapsed = (
            self.get_clock().now() - self.start_time
        ).nanoseconds / 1e9

        t = elapsed % 40.0

        # Simulated movement of the drone
        if t < 10.0:
            x = -3.0 + 0.6 * t
            y = -2.0
        elif t < 20.0:
            x = 3.0
            y = -2.0 + 0.4 * (t - 10.0)
        elif t < 30.0:
            x = 3.0 - 0.6 * (t - 20.0)
            y = 2.0
        else:
            x = -3.0
            y = 2.0 - 0.4 * (t - 30.0)

        # -------------------------------------------------
        # TF 1: map -> base_link
        # -------------------------------------------------
        base_tf = TransformStamped()

        base_tf.header.stamp = self.get_clock().now().to_msg()
        base_tf.header.frame_id = 'map'
        base_tf.child_frame_id = 'base_link'

        base_tf.transform.translation.x = x
        base_tf.transform.translation.y = y
        base_tf.transform.translation.z = 0.0

        base_tf.transform.rotation.x = 0.0
        base_tf.transform.rotation.y = 0.0
        base_tf.transform.rotation.z = 0.0
        base_tf.transform.rotation.w = 1.0

        # -------------------------------------------------
        # TF 2: base_link -> camera_link
        # -------------------------------------------------
        camera_tf = TransformStamped()

        camera_tf.header.stamp = self.get_clock().now().to_msg()
        camera_tf.header.frame_id = 'base_link'
        camera_tf.child_frame_id = 'camera_link'

        camera_tf.transform.translation.x = 0.100
        camera_tf.transform.translation.y = 0.0
        camera_tf.transform.translation.z = 0.020

        camera_tf.transform.rotation.x = 0.0
        camera_tf.transform.rotation.y = 0.0
        camera_tf.transform.rotation.z = 0.0
        camera_tf.transform.rotation.w = 1.0

        # Publish both transforms
        self.tf_broadcaster.sendTransform(base_tf)
        self.tf_broadcaster.sendTransform(camera_tf)


def main(args=None):
    rclpy.init(args=args)
    node = RobotMotion()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()