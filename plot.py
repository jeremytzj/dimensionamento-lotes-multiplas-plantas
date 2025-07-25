import matplotlib.pyplot as plt
import numpy as np

# Data provided
t_adicionais = np.array([0, 1, 2, 3, 4])
custo_total = np.array([42372522.59, 55592003.17, 71948736.19, 85983801.55, 97243377.37])
demanda_atendida = np.array([42.65, 52.88, 63.83, 72.02, 79.03])

# Convert runtime to seconds for easier plotting
# 10s = 10
# 1m20s = 80
# 3m = 180
# 68m = 4080
runtime_seconds = np.array([10, 10, 80, 180, 4080])

# Create figure and axes objects
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Custo Total on primary y-axis (ax1)
ax1.plot(t_adicionais, custo_total / 1e6, 'o-', color='tab:blue', label='Custo Total (Milhões BRL)')
ax1.set_xlabel('t Adicionais')
ax1.set_ylabel('Custo Total (Milhões BRL)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.grid(True, linestyle='--', alpha=0.6)

# Create a second y-axis for % Demanda Atendida and Runtime
ax2 = ax1.twinx()

# Plot % Demanda Atendida on secondary y-axis (ax2)
ax2.plot(t_adicionais, demanda_atendida, 's-', color='tab:green', label='% Demanda Atendida')
ax2.set_ylabel('% Demanda Atendida', color='tab:green')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Create a third y-axis for Runtime (sharing the same x-axis as ax1 and ax2)
# We'll use a different scale for runtime if needed, but for now, let's see how it looks.
# Alternatively, if runtime scale is too different, you might consider a log scale or a separate plot.
ax3 = ax1.twinx()
# Offset the spine of ax3 to the right to avoid overlapping with ax2
ax3.spines['right'].set_position(('outward', 60)) # Adjust 60 based on your preference

ax3.plot(t_adicionais, runtime_seconds, 'D-', color='tab:red', label='Runtime (Segundos)')
ax3.set_ylabel('Runtime (Segundos)', color='tab:red')
ax3.tick_params(axis='y', labelcolor='tab:red')


# Add a title
plt.title('Comparativo de Custo, Demanda Atendida e Runtime vs. t Adicionais')

# Add legends from all axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax3.legend(lines + lines2 + lines3, labels + labels2 + labels3, loc='upper left', bbox_to_anchor=(1.15, 1))

# Adjust layout to prevent labels from overlapping
fig.tight_layout()

# Show the plot
plt.show()