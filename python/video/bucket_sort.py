from manim import *

class BucketSortPro(Scene):
    def construct(self):
        # --- CONFIGURACIÓN INICIAL ---
        self.camera.background_color = "#1e1e1e" # Fondo oscuro suave
        
        title = Text("Bucket Sort", font_size=50, weight=BOLD, gradient=(BLUE, TEAL))
        title.to_edge(UP)
        self.play(Write(title))

        # Datos
        values = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
        num_buckets = 5
        
        # --- PASO 1: EL ARRAY ---
        # Crear representación visual del array
        array_group = VGroup()
        for val in values:
            square = Square(side_length=0.8, fill_opacity=1, color=WHITE)
            square.set_fill(TEAL_E, opacity=0.8)
            text = Text(f"{val:.2f}", font_size=22)
            item = VGroup(square, text)
            array_group.add(item)
            
        array_group.arrange(RIGHT, buff=0.1)
        array_group.to_edge(UP, buff=1.5)
        
        label_arr = Text("Array Original (Distribución Uniforme [0, 1))", font_size=24, color=GRAY)
        label_arr.next_to(array_group, UP)
        
        self.play(FadeIn(label_arr), DrawBorderThenFill(array_group))
        self.wait()

        # --- PASO 2: CREAR BUCKETS ---
        buckets = VGroup()
        bucket_labels = VGroup()
        
        # Crear buckets visualmente atractivos (tipo "U")
        for i in range(num_buckets):
            # Usamos líneas para formar una U
            bottom = Line(LEFT*0.6, RIGHT*0.6, color=WHITE)
            left = Line(bottom.get_start(), bottom.get_start() + UP*1.5, color=WHITE)
            right = Line(bottom.get_end(), bottom.get_end() + UP*1.5, color=WHITE)
            bucket_shape = VGroup(left, bottom, right)
            bucket_shape.set_color(BLUE_B)
            
            label = MathTex(f"B_{{{i}}}", color=YELLOW).next_to(bottom, DOWN)
            range_text = Text(f"[{i/num_buckets:.1f} - {(i+1)/num_buckets:.1f})", font_size=14, color=GRAY)
            range_text.next_to(label, DOWN, buff=0.1)
            
            group = VGroup(bucket_shape, label, range_text)
            buckets.add(group)
            bucket_labels.add(label) # Referencia rápida

        buckets.arrange(RIGHT, buff=0.5)
        buckets.to_edge(DOWN, buff=0.5)
        
        self.play(
            LaggedStart(*[Create(b) for b in buckets], lag_ratio=0.1),
            run_time=2
        )
        
        # Mostrar fórmula de índice
        formula_box = Rectangle(height=1.5, width=6, color=YELLOW, fill_opacity=0.1)
        formula_box.move_to(LEFT * 3)
        formula_text = MathTex(r"\text{Index} = \lfloor \text{valor} \times N \rfloor", font_size=36)
        formula_text.move_to(ORIGIN) # Centro temporal
        
        self.play(Create(formula_box), Write(formula_text))
        self.play(formula_box.animate.scale(0.7).to_edge(RIGHT).shift(UP*1), 
                  formula_text.animate.scale(0.7).to_edge(RIGHT).shift(UP*1))
        
        # --- PASO 3: DISTRIBUCIÓN ---
        bucket_contents = [[] for _ in range(num_buckets)]
        
        for i, item in enumerate(array_group):
            val = values[i]
            idx = int(val * num_buckets)
            
            # Resaltar el elemento actual
            self.play(item.animate.set_color(YELLOW).scale(1.1), run_time=0.3)
            
            # Mostrar el cálculo
            calc_text = MathTex(
                f"\\lfloor {val:.2f} \\times {num_buckets} \\rfloor = {idx}", 
                color=YELLOW, font_size=30
            )
            calc_text.next_to(formula_text, DOWN)
            self.play(Write(calc_text), run_time=0.5)
            
            # Mover al bucket
            target_bucket = buckets[idx][0] # La forma U
            # Calcular posición en stack
            stack_height = len(bucket_contents[idx])
            target_pos = target_bucket.get_bottom() + UP * (0.4 + stack_height * 0.5)
            
            self.play(
                item.animate.scale(0.8).move_to(target_pos).set_color(WHITE),
                run_time=0.7
            )
            self.play(Indicate(buckets[idx][1]), run_time=0.3) # Indicar etiqueta B_i
            
            bucket_contents[idx].append(item)
            self.play(FadeOut(calc_text), run_time=0.2)

        self.play(FadeOut(array_group), FadeOut(formula_box), FadeOut(formula_text), FadeOut(label_arr))

        # --- PASO 4: ORDENAMIENTO INTERNO (INSERTION SORT VISUAL) ---
        sort_text = Text("Ordenando cada bucket...", font_size=30, color=GREEN).to_edge(UP)
        self.play(Write(sort_text))

        sorted_final_list = []

        for b_idx, content in enumerate(bucket_contents):
            if not content: continue
            
            # Resaltar bucket actual
            self.play(buckets[b_idx][0].animate.set_color(GREEN), run_time=0.3)
            
            # Lógica visual de Insertion Sort simple
            # Extraemos los valores numéricos para ordenar la lista de objetos
            # Nota: Esto es una simulación visual, no el algoritmo completo paso a paso para ahorrar tiempo
            vals_in_bucket = [(float(item[1].text), item) for item in content]
            vals_in_bucket.sort(key=lambda x: x[0])
            
            sorted_mobjects = [x[1] for x in vals_in_bucket]
            
            # Reorganizar visualmente
            anims = []
            for stack_idx, mob in enumerate(sorted_mobjects):
                target_pos = buckets[b_idx][0].get_bottom() + UP * (0.4 + stack_idx * 0.5)
                anims.append(mob.animate.move_to(target_pos).set_color(GREEN_B))
            
            if anims:
                self.play(*anims, run_time=0.8)
            
            bucket_contents[b_idx] = sorted_mobjects # Actualizar referencia
            sorted_final_list.extend(sorted_mobjects)
            self.wait(0.2)

        # --- PASO 5: RECOLECCIÓN ---
        self.play(FadeOut(sort_text))
        concat_text = Text("Concatenación", font_size=30, color=TEAL).to_edge(UP)
        self.play(Write(concat_text))

        final_group = VGroup()
        for item in sorted_final_list:
            final_group.add(item)
            
        # Mover todo al centro en una línea
        self.play(
            final_group.animate.arrange(RIGHT, buff=0.1).move_to(ORIGIN).scale(1.25),
            FadeOut(buckets),
            run_time=2
        )
        
        # Caja final
        final_border = SurroundingRectangle(final_group, color=YELLOW, buff=0.2)
        self.play(Create(final_border))
        
        self.wait(2)