import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NormalComponent } from './normal.component';
import { LinksComponent } from '../links/links.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

describe('NormalComponent', () => {
  let component: NormalComponent;
  let fixture: ComponentFixture<NormalComponent>;

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [LinksComponent, NormalComponent],
      imports: [FontAwesomeModule]
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NormalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
