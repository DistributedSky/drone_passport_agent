from rosbag import Bag
from std_msgs.msg import String

bag = Bag("objective.bag", "w")

bag.write('/email', String('vadim.razorq@gmail.com'))
bag.write('/pilot_name', String('Vadim Manaenko'))
bag.write('/pilot_reg', String('123456'))
bag.write('/id_serial', String('INTCJ123-4567-890'))
bag.write('/id_reg', String('FA123456789'))
bag.write('/drone_type', String('VTOL'))
bag.write('/drone_make', String('DJI'))
bag.write('/drone_model', String('Matrice 100'))

bag.close()

