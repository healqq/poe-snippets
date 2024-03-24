import numpy as np
import random
import math
import matplotlib.pyplot as plt
import os

def get_bounce(prev_position, chaining_range): 
  angle = 2 * math.pi * random.random()
  return [
    prev_position[0] + math.cos(angle) * chaining_range, 
    prev_position[1] + math.sin(angle) * chaining_range
  ]


def distance(target, position):
   return math.sqrt((target[0] - position[0]) ** 2 + (target[1] - position[1]) ** 2)


def run_experiment_for_hitbox(hitbox_radius, experiments_count, hit_count):

  hit_radius = 180
  chaining_range = 0.5 * hit_radius
  enemy_pos = [1000, 1000]
  enemy_hitbox_radius = hitbox_radius


  # 2 coordiantes + hit metric
  experiments = np.zeros((experiments_count * hit_count, 3))

  for experiment_index in range(0, experiments_count):

    padding = experiment_index * hit_count
    # init throw
    experiments[padding] = enemy_pos + [1]

    remaining_chains = hit_count - 1
    current_hit_count = 1
    while remaining_chains > 0:
      next_position = get_bounce(experiments[padding + current_hit_count - 1], chaining_range)

      is_hit = distance(enemy_pos, next_position) < enemy_hitbox_radius + hit_radius

      experiments[padding + current_hit_count] = next_position + [is_hit]
      
      remaining_chains = remaining_chains - 1
      current_hit_count = current_hit_count + 1


  
  x = experiments[:, 0]
  y = experiments[:, 1]
  c = experiments[:, 2]


  return x,y,c





def main():
  experiments_count = 10000
  hit_count = 8

  for hitbox_radius in [20, 40, 60, 80, 100]:
    x,y,is_hit = run_experiment_for_hitbox(hitbox_radius, experiments_count, hit_count)
    hit_percentage = np.sum(is_hit) / experiments_count / hit_count * 100
    hit_box_circle = plt.Circle((1000, 1000), hitbox_radius, color='green', fill=False)
    c = np.array(list(map(lambda v: 'red' if v == 1 else 'blue', is_hit)))

    fig = plt.figure(num=hitbox_radius)
    ax = fig.gca()

    ax.scatter(x, y, c=c, s=1)
    ax.add_patch(hit_box_circle)
    ax.set_xlim(400, 1600)
    ax.set_ylim(400, 1600)
    ax.set_title('Hit distribution on {hitbox_radius:1.1f}m hit box radius. {hit_percentage:d}% hit percentage'.format(hitbox_radius=hitbox_radius/100, hit_percentage=int(hit_percentage)))
    fig.savefig('{path}/plot_{hitbox_radius:1.1f}m_half_chain_range.png'.format(
      path=os.path.dirname(os.path.realpath(__file__)), 
      hitbox_radius=hitbox_radius/100
    ))

    print('hit_rate is {rate:d}% for {hitbox_radius:1.1f}'.format(hitbox_radius=hitbox_radius/100, rate=int(hit_percentage)))

    
if __name__ == "__main__":
    main()
