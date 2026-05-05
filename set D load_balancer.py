# Simulated servers
servers = {
    "Server1": 0,
    "Server2": 0,
    "Server3": 0
}

requests = ["Req1", "Req2", "Req3", "Req4", "Req5", "Req6"]

print("=== ROUND ROBIN ===")
server_list = list(servers.keys())

for i, req in enumerate(requests):
    server = server_list[i % len(server_list)]
    servers[server] += 1
    print(f"{req} → {server}")

# Reset loads
servers = {k: 0 for k in servers}

print("\n=== LEAST CONNECTION ===")

for req in requests:
    # Find server with minimum load
    server = min(servers, key=servers.get)
    servers[server] += 1
    print(f"{req} → {server}")