try:
            try:
                choose = int(input("""
                    Welcome to Medical diagnosis expert system.

                    Specify which organ or specialization you would like to diagnose

                    1. Ear, Nose, and Throat (ENT) Diseases
                    2. Dental and Oral Diseases
                    3. Musculoskeletal Diseases
                    4. Cardiopulmonary Diseases
                    5. Gastrointestinal Diseases
                    6. Neurological Diseases
                    7. Endocrine Diseases
                    8. Urogenital Diseases
                    9. Ophthalmic Diseases
                    10. Dermatological Diseases

                    Choose from (1 - 10)
                    """))
            except RangeError as e:
                print(e.message)
        except ValueError:
            print("Only Integer numbers are valid")
