def count_jumps_on(clouds: []) -> int:
    jumps = 0
    cloud_index = 0
    while cloud_index < len(clouds):
        if is_second_next_cloud_safe(cloud_index, clouds):
            jumps += 1
            cloud_index += 2
            continue

        if is_next_cloud_safe(cloud_index, clouds):
            jumps += 1
            cloud_index += 1
            continue

        cloud_index += 1  # for final cloud

    return jumps


def is_second_next_cloud_safe(cloud_index, clouds) -> bool:
    clouds_boundary = len(clouds) - 1
    target_cloud = cloud_index + 2
    target_cloud_exists = target_cloud <= clouds_boundary

    return target_cloud_exists and is_cloud_safe(target_cloud, clouds)


def is_next_cloud_safe(cloud_index, clouds) -> bool:
    clouds_boundary = len(clouds) - 1
    target_cloud = cloud_index + 1
    target_cloud_exists = target_cloud <= clouds_boundary

    return target_cloud_exists and is_cloud_safe(target_cloud, clouds)


def is_cloud_safe(cloud_index, clouds) -> bool:
    return True if clouds[cloud_index] == 0 else False
