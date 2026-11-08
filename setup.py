from setuptools import setup

package_name = 'slam_doctor'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'numpy'],
    zip_safe=True,
    maintainer='darshmenon',
    maintainer_email='darshmenon02@gmail.com',
    description='Runtime health monitor for any ROS 2 SLAM.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={'console_scripts': ['slam_doctor = slam_doctor.doctor:main']},
)
