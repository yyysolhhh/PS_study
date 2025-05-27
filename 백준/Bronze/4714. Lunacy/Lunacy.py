while True:
    X = float(input())
    if X < 0:
        break
    print(f"Objects weighing {X:.2f} on Earth will weigh {0.167 * X:.2f} on the moon.")