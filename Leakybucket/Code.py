def leaky_bucket():
    # Take inputs
    bucket_size = int(input("Enter bucket size (max capacity): "))
    output_rate = int(input("Enter output rate (packets per second): "))
    n = int(input("Enter number of packets: "))

    packets = []
    for i in range(n):
        arrival_time = int(input(f"Enter arrival time of packet {i+1}: "))
        packet_size = int(input(f"Enter size of packet {i+1}: "))
        packets.append((arrival_time, packet_size))

    # Simulation
    current_bucket = 0
    current_time = 0

    print("\n--- Leaky Bucket Simulation ---")

    for arrival_time, packet_size in packets:
        # Leak packets between arrivals
        time_elapsed = arrival_time - current_time
        leaked = min(current_bucket, time_elapsed * output_rate)
        current_bucket -= leaked
        current_time = arrival_time

        print(f"\nTime {arrival_time}s:")
        print(f"Packet of size {packet_size} arrives.")
        print(f"Bucket before arrival: {current_bucket}")

        # Try to add packet
        if packet_size + current_bucket > bucket_size:
            print(f"Bucket overflow! Packet of size {packet_size} is dropped.")
        else:
            current_bucket += packet_size
            print(f"Packet added. Bucket now has {current_bucket} units.")

        # Send out packets according to output rate
        sent = min(current_bucket, output_rate)
        current_bucket -= sent
        print(f"Sent out {sent} units. Bucket now has {current_bucket} left.")

    # Empty remaining bucket
    while current_bucket > 0:
        current_time += 1
        sent = min(current_bucket, output_rate)
        current_bucket -= sent
        print(f"\nTime {current_time}s: Sent out {sent} units. Bucket now has {current_bucket} left.")

# Run simulation
leaky_bucket()
