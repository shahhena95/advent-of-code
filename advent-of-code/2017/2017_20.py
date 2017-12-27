import sys
import aocd
sys.path.insert(0, "/Library/Python/2.7/site-packages") #acod
sys.path.insert(0, "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python") #acod dependency


data = aocd.get_data("53616c7465645f5f51687d84c2dfe78a29cc10b8f7229b420668017a5b0fabfaeb360c5a2cd461d5f5898982f5a5db94", 20, 2017)


def process_data(data):
    data = [line.split(', ') for line in data.split('\n')]
    processed_data = []
    for line in data:
        each = []
        for particle in line:
            each.append(map(int, particle[3:-1].split(',')))
        
        processed_data.append(each)
    return processed_data
    
data = process_data(data)    


def man_dist(particle):
    position = particle[0]
    return sum([abs(x) for x in position])


def destroy_particles(data):
    duplicates = set()
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if data[i][0] == data[j][0]:
                duplicates.add(i)
                duplicates.add(j)

    for index in sorted(duplicates, reverse=True):
        del data[index]
    return data


def tick(particle):
    position, velocity, acceleration = particle[0], particle[1], particle[2]
    velocity[0] += acceleration[0]
    velocity[1] += acceleration[1]
    velocity[2] += acceleration[2]
    
    position[0] += velocity[0]
    position[1] += velocity[1]
    position[2] += velocity[2]
    
    particle[0], particle[1], particle[2] = position, velocity, acceleration
    return particle


# part 1
def z_buffering(data):
    count = 0
    long_term = False
    while count < 1500:
        data = map(tick, data)
        distances = map(man_dist, data)
        nearest = distances.index(min(distances))
        if not long_term or long_term != nearest:
            long_term = nearest
            count = 0
        elif long_term == nearest:
            count += 1
    return long_term

print(z_buffering(data))


#part 2
def remove_collision(data):
    count = 0
    while count < 500:
        data = map(tick, data)
        # data = list(map(destroy_particles, data))
        data = destroy_particles(data)

        count += 1

    return len(data) 

print(remove_collision(data))

