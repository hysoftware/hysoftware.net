import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeadComponent } from './dead.component';
import { LinksComponent } from '../links/links.component';

describe('DeadComponent', () => {
  let component: DeadComponent;
  let fixture: ComponentFixture<DeadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [DeadComponent, LinksComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
