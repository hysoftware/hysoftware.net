import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MatTableModule } from '@angular/material/table';

import { JPASCTComponent } from './jpasct.component';

describe('JPASCTComponent', () => {
  let component: JPASCTComponent;
  let fixture: ComponentFixture<JPASCTComponent>;
  let columns: string[] = [
    '名前', '所在地、電話番号、及びメールアドレス',
    '運営統括責任者', '追加手数料等の追加料金',
    '交換および返品（返金ポリシー）',
    '引渡時期', '受け付け可能な決済手段',
    '決済期間', '販売価格'
  ];

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [MatTableModule],
      declarations: [JPASCTComponent]
    });
    fixture = TestBed.createComponent(JPASCTComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('src has enough columns', () => {
    expect(component.src.map((el) => { return el.key; })).toEqual(columns);
  });
});
