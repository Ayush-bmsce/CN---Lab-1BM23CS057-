# Leaky Bucket Algorithm for Congestion Control

bucket_size = int(input("Enter bucket capacity (in packets): "))
leak_rate = int(input("Enter leak rate per second: "))
n = int(input("Enter number of incoming packets: "))

incoming = []
print("Enter packet sizes:")
for _ in range(n):
    incoming.append(int(input()))

stored = 0  # packets currently in bucket

print("\n--- Leaky Bucket Simulation ---")
for i in range(n):
    print(f"\nIncoming packet: {incoming[i]} packets")

    # Add incoming packets
    if stored + incoming[i] > bucket_size:
        dropped = (stored + incoming[i]) - bucket_size
        stored = bucket_size
    else:
        dropped = 0
        stored += incoming[i]

    print("Stored in bucket:", stored)
    print("Dropped packets:", dropped)

    # Leak packets
    leaked = min(stored, leak_rate)
    stored -= leaked
    print("Leaked out:", leaked)
    print("Remaining in bucket:", stored)

print("\nSimulation complete.")
