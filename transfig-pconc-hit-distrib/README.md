# Average overlaps count for poisonous concoction of

Transfigured [Poisonous concoction](https://www.poewiki.net/wiki/Poisonous_Concoction) jumps in random direction on hitting terrain, if there are remaining chain.
This simulation plots a typical situation to estimate number of overlaps based on target hit box.

Hit box sizes used are in range of 0.2m - 1m, 0.2m being a humanoid hitbox (smallest possible?).
Chains amount is 7 (8 hits total).

# TLDR

~ 43% overlaps or more if chaining range = pconc radius
~ 75% overlaps or more if chaining range = 50% of pconc radius

# Plots

If chaining range matches pconc radius

## 0.2m enemy hitbox

![visualisation](plot_0.2m.png)

## 0.4m enemy hitbox

![visualisation](plot_0.4m.png)

## 0.6m enemy hitbox

![visualisation](plot_0.6m.png)

## 0.8m enemy hitbox

![visualisation](plot_0.8m.png)

## 1.0m enemy hitbox

![visualisation](plot_1.0m.png)

# Plots

If chaining range is half of pconc radius

## 0.2m enemy hitbox

![visualisation](plot_0.2m_half_chain_range.png)

## 0.4m enemy hitbox

![visualisation](plot_0.4m_half_chain_range.png)

## 0.6m enemy hitbox

![visualisation](plot_0.6m_half_chain_range.png)

## 0.8m enemy hitbox

![visualisation](plot_0.8m_half_chain_range.png)

## 1.0m enemy hitbox

![visualisation](plot_1.0m_half_chain_range.png)
