import Std

/-! Algebra behind the pointwise support derivative. Analytic arguments are in the paper. -/
namespace BidiskVariation
open Lean.Grind

def dot {R : Type} [CommRing R] (x₁ x₂ y₁ y₂ : R) : R := x₁*y₁ + x₂*y₂

theorem cornerGradient {R : Type} [CommRing R] (x y c d : R) (h : d = 0) :
    -(y*c) + d*x = -(c*y) ∧ -(x*c) - d*y = -(c*x) := by
  subst d
  constructor <;> grind

theorem supportVelocity {R : Type} [CommRing R] (a b x₁ x₂ y₁ y₂ : R) :
    (a*x₁)*(-(dot x₁ x₂ y₁ y₂*y₁)) + (a*x₂)*(-(dot x₁ x₂ y₁ y₂*y₂)) +
    (b*y₁)*(-(dot x₁ x₂ y₁ y₂*x₁)) + (b*y₂)*(-(dot x₁ x₂ y₁ y₂*x₂)) =
    -(a+b)*(dot x₁ x₂ y₁ y₂)^2 := by
  unfold dot
  grind

theorem quarterTurn {R : Type} [CommRing R] (x₁ x₂ y₁ y₂ : R) :
    (dot x₁ x₂ y₁ y₂)^2 + (dot x₁ x₂ (-y₂) y₁)^2 =
    (x₁^2+x₂^2)*(y₁^2+y₂^2) := by
  unfold dot
  grind

theorem workedDirection :
    (3/5 : Rat)^2 + (4/5)^2 = 1 ∧
    -(3/5+4/5 : Rat)*(3/5)^2 = -63/125 ∧
    2*(-63/125 : Rat) = -126/125 := by decide +kernel

theorem normalizedMean :
    2*(2/3+2/3 : Rat) = 8/3 ∧ -2*(2/3+2/3 : Rat)*(1/2) = -4/3 := by decide +kernel

#print axioms cornerGradient
#print axioms supportVelocity
#print axioms quarterTurn
#print axioms workedDirection
#print axioms normalizedMean

end BidiskVariation
