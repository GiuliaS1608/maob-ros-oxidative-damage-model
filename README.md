# Mathematical Modeling of MAO-B-Mediated Reactive Oxygen Species (ROS) Production and Oxidative Damage
**Language:** English | [Português](README-pt.md)

A dynamic and semiquantitative mathematical model based on ordinary differential equations (ODEs) for investigating reactive oxygen species (ROS) production mediated by monoamine oxidase B (MAO-B) and its relationship with oxidative damage.

The model represents the temporal cascade linking dopamine metabolism, hydrogen peroxide ($\mathrm{H_2O_2}$), ROS formation, and oxidative damage. It is intended primarily for exploring relative changes in system behavior under different parametric perturbations rather than predicting absolute intracellular concentrations.

## Overview

Oxidative stress results from an imbalance between the production of reactive oxygen species and the cellular capacity to neutralize them. In this model, dopamine metabolism by MAO-B is represented as an initial source of $\mathrm{H_2O_2}$, which is subsequently linked to ROS formation and oxidative damage.

The model was designed to investigate how changes in:

- effective MAO-B activity;
- dopamine availability;
- antioxidant capacity; and
- cellular damage repair/removal

modify the temporal dynamics of the oxidative cascade.

## Mathematical Model

The initial enzymatic step is described by Michaelis-Menten kinetics:

$$
V(S)=\frac{V_{\max}^{*}S}{K_m+S}
$$

The complete dynamic model is:

$$
\frac{dS}{dt} = P-\frac{V_{\max}^{*}S}{K_m+S}-K_sS,
$$

$$
\frac{dH}{dt} = \alpha\frac{V_{\max}^{*}S}{K_m+S}-K_hH,
$$

$$
\frac{dR}{dt} =\beta H-K_rR,
$$

$$
\frac{dD}{dt} = \gamma R-K_dD.
$$

The pathway represented by the model can be summarized as:

**Dopamine $S(t)$ $\to$ MAO-B-mediated metabolism $\to$ $\mathrm{H_2O_2}$ $H(t)$ $\to$ ROS $R(t)$ $\to$ Oxidative damage $D(t)$**

MAO-B is not modeled as an independent state variable. Its effective activity is represented through the Michaelis-Menten term containing $V_{\max}^{*}$ and $K_m$.

## Model Variables

| Variable | Description | Unit |
|---|---|---|
| $S(t)$ | Dopamine concentration | $\mu\mathrm{M}$ |
| $H(t)$ | Normalized $\mathrm{H_2O_2}$ level | arbitrary units |
| $R(t)$ | Normalized ROS level | arbitrary units |
| $D(t)$ | Oxidative damage level | arbitrary units |

Because $H(t)$, $R(t)$, and $D(t)$ are expressed as relative indices, the model is **semiquantitative**. These variables should not be interpreted as absolute intracellular concentrations.

## Basal Parameters

| Parameter | Value | Unit | Interpretation |
|---|---:|---|---|
| $K_m$ | 229 | $\mu\mathrm{M}$ | Michaelis-Menten constant |
| $V_{\max}^{*}$ | 100 | $\mu\mathrm{M}\,\mathrm{min}^{-1}$ | Effective maximum reaction rate |
| $P$ | 50 | $\mu\mathrm{M}\,\mathrm{min}^{-1}$ | Basal dopamine production |
| $K_s$ | 0.7 | $\mathrm{min}^{-1}$ | Additional physiological dopamine removal |
| $\alpha$ | 1.0 | — | Effective $\mathrm{H_2O_2}$ formation/conversion factor |
| $K_h$ | 0.5 | $\mathrm{min}^{-1}$ | $\mathrm{H_2O_2}$ removal |
| $\beta$ | 0.8 | $\mathrm{min}^{-1}$ | Effective ROS formation rate |
| $K_r$ | 0.7 | $\mathrm{min}^{-1}$ | ROS neutralization |
| $\gamma$ | 0.6 | — | Effective oxidative damage formation/conversion factor |
| $K_d$ | 0.9 | $\mathrm{min}^{-1}$ | Damage repair/removal |

The parameters $\alpha$ and $\gamma$ are treated as effective conversion factors between variables represented on different scales. Because $H(t)$, $R(t)$, and $D(t)$ are semiquantitative variables expressed in arbitrary units, no explicit physical unit is assigned to these parameters. The symbol "—" therefore indicates that a physical unit is not specified within the current semiquantitative formulation, rather than implying that the parameter is necessarily dimensionless.

The initial conditions are:

$$
S(0)=200\ \mu\mathrm{M},\qquad
H(0)=0,\qquad
R(0)=0,\qquad
D(0)=0.
$$

Except for $K_m$, the parameters are primarily effective model parameters chosen to represent the qualitative behavior of the proposed cascade. In particular, $\alpha$ and $\gamma$ act as effective conversion factors between variables represented on different scales.

## Simulation Scenarios

Five predefined conditions are considered.

| Scenario | Parameter change |
|---|---|
| Basal | Reference values |
| Increased MAO-B activity | $V_{\max}^{*}: 100 \rightarrow 500$ |
| Increased dopamine production | $P: 50 \rightarrow 90$ |
| Antioxidant deficiency | $K_h: 0.5 \rightarrow 0.2$ and $K_r: 0.7 \rightarrow 0.3$ |
| Reduced repair | $K_d: 0.9 \rightarrow 0.2$ |

### Basal

The basal condition is used as the reference state. Dopamine, $\mathrm{H_2O_2}$, ROS, and oxidative damage evolve toward a stable regime determined by the balance between production and removal terms.

### Increased MAO-B Activity

The effective maximum velocity is increased fivefold. This increases dopamine consumption through the MAO-B-mediated reaction and intensifies $\mathrm{H_2O_2}$ production, which propagates through the model to higher ROS and oxidative damage.

The fivefold increase is a **hypothetical parametric perturbation** used to explore the system response. It should not be interpreted as a direct experimental measurement of a specific pathological condition.

### Increased Dopamine Production

The dopamine production rate is increased from $50$ to $90\ \mu\mathrm{M}\,\mathrm{min}^{-1}$. Greater substrate availability sustains higher MAO-B-mediated metabolism and increases downstream $\mathrm{H_2O_2}$, ROS, and oxidative damage.

### Antioxidant Deficiency

The $\mathrm{H_2O_2}$ removal and ROS neutralization parameters are reduced. Dopamine dynamics remain similar to the basal condition, while $\mathrm{H_2O_2}$ and ROS remain elevated for longer periods, producing higher oxidative damage.

### Reduced Repair

The oxidative-damage repair/removal parameter is reduced. Because $K_d$ appears only in the equation for $D(t)$, dopamine, $\mathrm{H_2O_2}$, and ROS trajectories remain essentially unchanged relative to the basal condition, while oxidative damage accumulates to higher levels.

## Numerical Solution

The system is solved numerically using the classical fourth-order Runge-Kutta method (RK4).

The integration step used in the simulations is:

$$
h=0.05\ \mathrm{min},
$$

corresponding to $3\ \mathrm{s}$.

A comparison with $h=0.025\ \mathrm{min}$ did not produce relevant changes in the trajectories, supporting the use of $h=0.05\ \mathrm{min}$ for the simulations presented in the study.

Simulations generally use a $10\ \mathrm{min}$ interval. For antioxidant deficiency and reduced repair, the interval is extended to $20\ \mathrm{min}$ to better visualize their slower dynamics.

## Interactive Interface

The repository includes a Streamlit interface for interactively exploring the model.

The interface allows users to:

- select one of the predefined scenarios;
- compare a selected scenario with the basal condition;
- change the simulation time;
- inspect the temporal trajectories of all four state variables;
- visualize the parameters used in each simulation;
- create custom parameter combinations; and
- inspect a numerical summary of the simulated state.

The interactive application is intended as a computational and educational complement to the mathematical model.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd maob-ros-oxidative-damage-model
```

Create a virtual environment if desired, then install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Interface

From the repository root, run:

```bash
python -m streamlit run interface/app.py
```

Streamlit will start a local server and open the application in your browser.

## Repository Structure

```text
maob-ros-oxidative-damage-model/
-- README.md
-- requirements.txt
-- .gitignore

-- interface/
   -- app.py

-- octave/
   -- ...

-- figures/
   -- ...

-- docs/
   -- ...
```
-- LICENSE

## Model Scope and Limitations

This model is deliberately simplified and semiquantitative. Its main purpose is to investigate the temporal relationships among the mechanisms represented in the ODE system.

Important limitations include:

- $\mathrm{H_2O_2}$, ROS, and oxidative damage are represented as normalized or relative indices rather than absolute intracellular concentrations.
- Several parameters are effective model parameters and should not be interpreted as directly measurable biochemical constants.
- Antioxidant mechanisms are represented through aggregated removal/neutralization terms.
- Damage repair and removal processes are represented by a single effective term.
- The model describes temporal dynamics and does not explicitly represent spatial distribution or cellular compartments.
- The model does not attempt to reproduce the complete biochemical network associated with oxidative stress or neurodegeneration.

Accordingly, simulation results should primarily be interpreted in terms of **relative and qualitative changes between scenarios**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

**Giulia S. Ferreira**  
**Vinícius F. Wasques**  
**Juliana H. C. Smetana**

Ilum School of Science - Brazilian Center for Research in Energy and Materials (CNPEM), Campinas, São Paulo, Brazil.

## Reference

This repository accompanies the mathematical modeling work:

**Ferreira, G. S.; Wasques, V. F.; Smetana, J. H. C.**  
*Modelagem Matemática da Produção de Espécies Reativas de Oxigênio (ROS) Mediada pela MAO-B e sua Relação com Dano Oxidativo.*
