from equation import Equation


class RegulaFalsi(Equation):
    def solve_regula(self, section_a, section_b, error_limit):
        error = 100
        while error >= error_limit:
            interval = self.get_interval(section_a, section_b)
            # f_interval = self.solve(interval)
            if self.below_to_zero(section_a, interval):
                section_b = interval
            else:
                section_a = interval

            error = self.get_percentual_error(section_a, section_b)
            self.sections.append({'a': section_a,
                                  'b': section_b,
                                  'interval': interval,
                                  # 'f(interval)': f_interval,
                                  'error': error})

        return interval

    def get_interval(self, a, b):
        return (float(self.solve(a) * b) - (self.solve(b) * a)) / (self.solve(a) - self.solve(b))


if __name__ == '__main__':
    falsi = RegulaFalsi("((x)**3)+(4(x)**2)-10", 'x')
    print(falsi.solve_regula(1, 2, 0.2))
    print(falsi.get_sections())
