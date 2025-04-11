import os

import ament_index_python.packages
import launch
import launch.launch_description_sources
import launch_ros.actions


def generate_launch_description():
    ublox_launch_directory = os.path.join(
        ament_index_python.packages.get_package_share_directory('ublox_gps'),
        'launch'
    )
    
    
    ntrip_launch_directory = os.path.join(
        ament_index_python.packages.get_package_share_directory('ntrip_client')
    )
    
    

    ublox_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            ublox_launch_directory + '/ublox_gps_node-launch.py'))

    ntrip_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            ntrip_launch_directory + '/ntrip_client_launch.py'))

    return launch.LaunchDescription([
        ntrip_launch,
        ublox_launch
    ])
